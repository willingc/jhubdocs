# example showing sudo config
# docker run -it -p 9000:8000 jupyter/jupyterhub-sudo

FROM jupyter/jupyterhub

MAINTAINER Jupyter Project <jupyter@googlegroups.com>

# fix permissions on sudo executable (how did this get messed up?)
RUN chmod 4755 /usr/bin/sudo

# add the rhea user, who will run the server
# she needs to be in the shadow group in order to access the PAM service
RUN useradd -m -G shadow -p $(openssl passwd -1 rhea) rhea

# Give rhea passwordless sudo access to run the sudospawner mediator on behalf of users:
ADD examples/sudoers /tmp/sudoers
RUN cat /tmp/sudoers >> /etc/sudoers
RUN rm /tmp/sudoers

# add some regular users
RUN for name in io ganymede; do useradd -m -p $(openssl passwd -1 $name) $name; done

# make home directories private
RUN chmod o-rwx /home/*

ADD . /srv/sudospawn
WORKDIR /srv/sudospawn
RUN pip3 install .

# make the working dir owned by rhea, so she can create the state database
RUN chown rhea .

USER rhea
