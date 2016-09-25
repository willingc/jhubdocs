import os
import pwd
import time
import subprocess
from traitlets import Bool, Int, Unicode, List
from tornado import gen

from jupyterhub.spawner import Spawner
from jupyterhub.utils import random_port


class SystemdSpawner(Spawner):
    mem_limit = Unicode(
        '',
        help='Memory limit for each user. Set to \'\' (default) for no limits. Uses suffixes that are recognized by Systemd (M, G, etc)'
    ).tag(config=True)

    cpu_limit = Int(
        0,
        help='CPU limit for each user. 100 means 1 full CPU, 30 is 30% of 1 CPU, 200 is 2 CPUs, etc. Set to 0 (default) for no limits'
    ).tag(config=True)

    run_as_system_users = Bool(
        True,
        help='Run each service with the uid of the user it is authenticated as'
    ).tag(config=True)

    # FIXME: Do not allow enabling this for systemd versions < 227,
    # since that is when it was introduced.
    isolate_tmp = Bool(
        False,
        help='Give each notebook user their own /tmp, isolated from the system & each other'
    ).tag(config=True)

    user_workingdir = Unicode(
        '/home/{USERNAME}',
        help='Path to start each notebook user on. {USERNAME} and {USERID} are expanded'
    ).tag(config=True)

    default_shell = Unicode(
        os.environ.get('SHELL', '/bin/bash'),
        help='Default shell for users on the notebook terminal'
    ).tag(config=True)

    extra_paths = List(
        [],
        help='Extra paths to add to the $PATH environment variable. {USERNAME} and {USERID} are expanded',
    ).tag(config=True)

    unit_name_template = Unicode(
        'jupyter-{USERID}-singleuser',
        help='Template to use to make the systemd service names. {USERNAME} and {USERID} are expanded}'
    ).tag(config=True)

    @property
    def unit_name(self):
        return self._expand_user_vars(self.unit_name_template)

    def _expand_user_vars(self, string):
        """
        Expand user related variables in a given string

        Currently expands:
          {USERNAME} -> Name of the user
          {USERID} -> UserID
        """
        return string.format(
            USERNAME=self.user.name,
            USERID=self.user.id
        )

    @gen.coroutine
    def start(self):
        self.port = random_port()

        # if a previous attempt to start the service for this user was made and failed,
        # systemd keeps the service around in 'failed' state. This will prevent future
        # services with the same name from being started. While this behavior makes sense
        # (since if it fails & is deleted immediately, we will lose state info), in our
        # case it is ok to reset it and move on when trying to start again.
        try:
            if subprocess.check_output([
                '/bin/systemctl',
                'is-failed',
                self.unit_name
            ]).decode('utf-8').strip() == 'failed':
                subprocess.check_output([
                    '/bin/systemctl',
                    'reset-failed',
                    self.unit_name
                ])
                self.log.info('Found unit {unit} in failed state, reset state to inactive'.format(
                    unit=self.unit_name)
                )
        except subprocess.CalledProcessError as e:
            # This is returned when the unit is *not* in failed state. bah!
            pass
        env = self.get_env()

        cmd = ['/usr/bin/systemd-run']

        cmd.extend(['--unit', self.unit_name])
        if self.run_as_system_users:
            try:
                pwnam = pwd.getpwnam(self.user.name)
            except KeyError:
                self.log.exception('No user named %s found in the system' % self.user.name)
                raise
            cmd.extend(['--uid', str(pwnam.pw_uid), '--gid', str(pwnam.pw_gid)])

        if self.isolate_tmp:
            cmd.extend(['--property=PrivateTmp=yes'])

        if self.extra_paths:
            env['PATH'] = '{curpath}:{extrapath}'.format(
                curpath=env['PATH'],
                extrapath=':'.join(
                    [self._expand_user_vars(p) for p in self.extra_paths]
                )
            )

        for key, value in env.items():
            cmd.append('--setenv={key}={value}'.format(key=key, value=value))

        cmd.append('--property=WorkingDirectory={workingdir}'.format(
            workingdir=self._expand_user_vars(self.user_workingdir)
        ))

        cmd.append('--setenv=SHELL={shell}'.format(shell=self.default_shell))

        if self.mem_limit != '':
            # FIXME: Detect & use proper properties for v1 vs v2 cgroups
            cmd.extend([
                '--property=MemoryAccounting=yes',
                '--property=MemoryLimit={mem}'.format(mem=self.mem_limit),
            ])

        if self.cpu_limit != 0:
            # FIXME: Detect & use proper properties for v1 vs v2 cgroups
            # FIXME: Make sure that the kernel supports CONFIG_CFS_BANDWIDTH
            #        otherwise this doesn't have any effect.
            cmd.extend([
                '--property=CPUAccounting=yes',
                '--property=CPUQuota={quota}%'.format(quota=self.cpu_limit)
            ])

        cmd.extend([self._expand_user_vars(c) for c in  self.cmd])
        cmd.extend(self.get_args())

        self.log.debug('Running systemd-run with: %s' % ' '.join(cmd))
        subprocess.check_output(cmd)

        for i in range(self.start_timeout):
            is_up = yield self.poll()
            if is_up is None:
                return (self.ip or '127.0.0.1', self.port)
            time.sleep(1)

        return None

    @gen.coroutine
    def stop(self):
        subprocess.check_output([
            '/bin/systemctl',
            'stop',
            self.unit_name
        ])

    @gen.coroutine
    def poll(self):
        if hasattr(self, 'unit_name'):
            try:
                if subprocess.check_output([
                    '/bin/systemctl',
                    'is-active',
                    self.unit_name
                ]).decode('utf-8').strip() == 'active':
                    return None
            except subprocess.CalledProcessError as e:
                return e.returncode
        return 0
