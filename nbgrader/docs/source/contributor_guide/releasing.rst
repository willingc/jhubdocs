Releasing a new version
=======================

.. contents::
    :local:
    :depth: 1

Update the changelog
--------------------

Ideally, the :doc:`/changelog` (located at
``nbgrader/docs/source/changelog.rst``) should be updated as things are
changed. In practice, this doesn't always happen as people forget to include
changes to the changelog in PRs. However, the changelog should be fully
up-to-date at the time of a release. To ensure that it is up-to-date, filter
PRs on GitHub by the current milestone and make sure to include all major
changes. In addition, please include a full list of merged PRs, which can be
found using the ``changelog.py`` script in the ``tools`` directory, for
example::

    ./tools/changelog.py 0.3.0

This will print out the list of merged PRs for the given milestone, which
should then be included in the changelog.

Get the list of contributors
----------------------------

To get the list of contributors, you can use the ``contributor_list.py`` script
in the ``tools`` directory, for example::

    ./tools/contributer_list.py 0.3.0

This will print out the list of users who have submitted issues and/or PRs.
This list should then be included in the changelog.

Bump the version number
-----------------------

There are **two** locations where the version number needs to be changed. The
first is in ``nbgrader/_version.py``, and the second is in
``conda.recipe/meta.yaml``. Note that when you change the version number in the
conda recipe you should also reset the build number back to zero.

Rebuild the documentation
-------------------------

Regenerate all the documentation for this release by running::

    invoke docs

Make sure the linkcheck and spellcheck pass, and commit the results.

Make a PR
---------

At this point, make a pull request with the changes you have made so far. Make
sure all the tests pass. After this point, you shouldn't need to make any more
changes to the source: the remaining steps all have to do with building and
releasing packages and creating branches/tags on GitHub.

Clean all untracked files
-------------------------

Make sure there are no old files lying around the repository. First, see what
needs to be cleaned::

    git clean -ndx

After verifying this doesn't include anything important, clean them for real::

    git clean -fdx

Build and release the conda packages
------------------------------------

The recipe for the nbgrader conda package is located in the ``conda.recipe``
folder and should include all the necessary information about dependencies and
version. This should be kept up-to-date with the main ``setup.py`` in the root
of the repository.

To build the conda packages, you can use the script ``conda_build.sh`` in the
``tools`` directory. This will build a conda package for each supported version
of Python (currently, 2.7, 3.4, and 3.5) and run the full test suite (excluding
JupyterHub tests) in a fresh conda environment. This ensures that all the
necessary package files are actually being installed.

After the packages have been built, the script will convert them for all
available platforms (osx, linux, and windows). Finally, after converting the
packages, they will be uploaded to Anaconda Cloud.

Note that if anything goes wrong with the conda builds, you will need to increase the build number in the ``conda.recipe/meta.yaml`` file.

Build and release the pip package
---------------------------------

To build the pip package, run the ``release.py`` script in the ``tools``
directory::

    ./tools/release.py

This will do a few things, including converting the README file to rst (so it
will display correctly on PyPI), building the source distribution, installing
the source distribution into a temporary conda environment, and running tests
in that environment.

Once you have verified that the tests pass, you can upload the package to PyPI
with::

    python setup.py sdist upload

Create a git tag and possibly branch
------------------------------------

If this is a new major release, create a new ``.x`` branch. For example, if
this is the 0.3.0 release, create a branch called ``0.3.x``.

Additionally, regardless of whether this is a major release, create a tag for
the release. Release tags should be prefixed with ``v``, for example,
``v0.3.0``.

Create a release on GitHub
--------------------------

After pushing the tag (and branch, if necessary) to GitHub, create the actual
release on GitHub. To do this, go to
`https://github.com/jupyter/nbgrader/releases <https://github.com/jupyter/nbgrader/releases>`_
and click the button for "Draft a new release". Choose the tag you just created
and set the title as "nbgrader <tag>", where "<tag>" is the name of the tag
(e.g. v0.3.0). Put in the release notes, which should be pretty much the same
as what is in the changelog.

Change to development version
-----------------------------

Bump the version again, this time to development. For example, if the release
was ``0.3.0``, then the new version should be ``0.4.0.dev0``. As stated above,
there are **two** locations where the version number needs to be changed. The
first is in ``nbgrader/_version.py``, and the second is in
``conda.recipe/meta.yaml``. Note that when you change the version number in the
conda recipe you should also reset the build number back to zero.
