# Services


With version 0.7, JupyterHub adds support for 'Services'.


## JupyterHub's definition of a Service

When working with JupyterHub, a Service is defined as a process that interacts
with the Hub's REST API. A Service may perform a specialized action or
specific task. For example, each of these tasks can be a unique Service:

- shutting down individuals' single user notebook servers that have been idle
  for some time
- registering additional web servers which should use the Hub's authentication
  and be served behind the Hub's proxy.

Two main characteristics help define a Service:

1. Is the *Service* **managed** by JupyterHub?
2. Does the *Service* have a web server that should be added to the proxy's 
   table?

Currently, a Service may be either a 'Hub-Managed Service' which is managed by
JupyterHub, or an 'Externally-Managed Service' which runs its own web server and
communicates operation instructions via the Hub's API.

### Properties of a Service

If a `command` is specified for launching the Service, the Service will be
started and managed by the Hub.

If a `url` is specified for where the Service runs its own web server,
JupyterHub will add the Service to the Hub's proxy at 
`/service/:service-name`.

## Hub-Managed Service

If a Service is started by the Hub and the Hub is responsible for the
Service's actions, the Service is referred to as a **Hub-Managed Service** of 
JupyterHub. Hub-Managed Services can only be a local subprocesses of the Hub. The
Hub will take care of starting these processes and restarting them if they
stop.

While Hub-Managed Services share some similarities with notebook Spawners,
there are no plans for Hub-Managed Services to support the same spawning
abstractions as a notebook Spawner. If you wish to run Services in
Docker or other deployment environments, the Service can be registered as an
Externally-Managed Service, as described below.

### Launching a Hub-Managed Service

A Hub-Managed Service is characterized by its specified `command` for launching
the Service. For example, the configuration of a 'cull idle' notebook server
Hub-Managed Service would include the Service name, admin permissions, and the
`command` to launch the Service which will cull idle servers after a timeout
interval:

```python
c.JupyterHub.services = [
    {
        'name': 'cull-idle',
        'admin': True,
        'command': ['python', '/path/to/cull-idle.py', '--timeout']
    }
]
```


In addition to the `command` to launch the Service, a Hub-Managed Service may also
be configured with additional optional parameters, which describe the
environment needed to start the process:

- `env: dict` additional environment variables for the Service.
- `user: str` name of the user to run the server as if different from the Hub.
   Requires Hub to be root.
- `cwd: path` directory in which to run the Service, if different from the 
   Hub directory.

The Hub will pass the following environment variables to launch the Service:

```
JUPYTERHUB_SERVICE_NAME:   the name of the service
JUPYTERHUB_API_TOKEN:      API token assigned to the service
JUPYTERHUB_API_URL:        URL for the JupyterHub API (default, http://127.0.0.1:8080/hub/api)
JUPYTERHUB_BASE_URL:       Base URL of the Hub (https://mydomain[:port]/)
JUPYTERHUB_SERVICE_PREFIX: URL path prefix of this service (/services/:service-name/)
```

For the previous example, these environment variables would be passed when
starting the 'cull idle' Service:

```
JUPYTERHUB_SERVICE_NAME: 'cull-idle'
JUPYTERHUB_API_TOKEN: API token assigned to the service
JUPYTERHUB_API_URL: http://127.0.0.1:8080/hub/api
JUPYTERHUB_BASE_URL: https://mydomain[:port]
JUPYTERHUB_SERVICE_PREFIX: /services/cull-idle/
```

## Externally-Managed Services

To meet your specific use case needs, you may use your own service management
tools, such as Docker or systemd, to manage a JupyterHub Service.
These Externally-Managed Services, unlike Hub-Managed Services, are not subprocesses of
the Hub. You must tell JupyterHub which API token the Externally-Managed Service is
using to perform its API requests. Each Externally-Managed Service will need a unique
API token because the Hub authenticates each API request and the API token is
used to identify the originating Service or user.

A configuration example of an Externally-Managed Service with admin access and running its
own web server is:

```python
c.JupyterHub.services = [
    {
        'name': 'my-web-service',
        'url': 'https://10.0.1.1:1984',
        'api_token': 'super-secret',
    }
]
```


## Writing your own services

TODO

### Authenticating with the Hub

TODO

JupyterHub 0.7 introduces some utilities to use the Hub's authentication
mechanism.