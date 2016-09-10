.. JupyterHub Federated Docs documentation master file, created by
   sphinx-quickstart on Fri Sep  9 10:23:50 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

JupyterHub Federated Docs
=========================

:Date: |today|


.. note:: This is a documentation development project. Please refer to the
          official docs on readthedocs.io for each JupyterHub project.


Contents
--------

**Fundamentals:**

.. toctree::
    :titlesonly:
    :maxdepth: 1

    jupyterhub/docs/source/index
    configurable-http-proxy/README.md

**Authenticators:** Used to verify users and administrators

.. toctree::
    :titlesonly:
    :maxdepth: 1

    ldapauthenticator/README.md
    oauthenticator/README.md

**Spawners:** Used to create a single-user notebook server for a user

.. toctree::
    :titlesonly:
    :maxdepth: 1

    batchspawner/README.md
    dockerspawner/README.md
    sudospawner/README.md
    systemdspawner/README.md

**Reference Deployments:**

.. toctree::
    :titlesonly:
    :maxdepth: 1

    jupyterhub-deploy-docker/README.md
    jupyterhub-deploy-hpc/README.md

**Teaching Deployments:**

.. toctree::
    :titlesonly:
    :maxdepth: 1

    jupyterhub-deploy-teaching/docs/source/index
    nbgrader/nbgrader/docs/source/index


Helpful Resources
-----------------

* `Documentation <http://jhubdocs.readthedocs.io>`_
* `Gitter <https://gitter.im/jupyterhub/jupterhub>`_
* `Mailing list <https://groups.google.com/forum/#!forum/jupyter>`_
* `GitHub Repository <https://github.com/jupyterhub/jupyterhub>`_
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
