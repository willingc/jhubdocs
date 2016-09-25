#jhubdocs

A prototype "proof of concept" of federated docs for the JupyterHub organization

**Note: This is not the official JupyterHub documentation.**

Please refer to https://jupyterhub.readthedocs.io for the official documentation.

## Prototype notes

Proof of concept prototype rendered at https://jhubdocs.readthedocs.io/en/latest/.

The prototype uses git subtree.

## Development notes

To add a repo to the federated docs, create a remote to the repo and then
add the subtree:

    git remote add dockerspawner https://github.com/jupyterhub/dockerspawner
    git subtree add --squash --prefix=dockerspawner/ dockerspawner master

Don't forget the trailing '/' in the `--prefix` option or your directory
structure will be messed up. Do a `git log` if you are curious about what
has been done by the `git subtree` command.

### To update docs

Over time, the subtrees will have changes. To update the federated docs:

- Get the changes from the subtree

    ```bash
    git subtree pull --squash --prefix=systemdspawner/ systemdspawner master
    ```

- Merge the commit when prompted to do so.

- When done with each changed subtree, push changes to the origin repo:

    ```bash
    git push origin master
    ```

## Known issues

- Auto doc of API and modules is not supported in the prototype.
- Auto generated documentation of config files is not implemented in the
  prototype
