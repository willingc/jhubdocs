.. _changelog:

Changelog
=========

A summary of changes to nbgrader.

0.3.0
-----

Version 0.3.0 of nbgrader introduces several significant changes. Most notably,
this includes:

- Windows support
- Support for Python 3.5
- Support for Jupyter Notebook 4.2
- Allow assignments and students to be specified in ``nbgrader_config.py``
- Addition of the "nbgrader quickstart" command
- Addition of the "nbgrader extension uninstall" command
- Create a nbgrader conda recipe
- Add an entrypoint for late penalty plugins

The full list of merged PRs is:

- PR #521: Update to most recent version of invoke
- PR #512: Late penalty plugin
- PR #510: Fix failing windows tests
- PR #508: Run notebook/formgrader/jupyterhub on random ports during tests
- PR #507: Add a FAQ
- PR #506: Produce a warning if no coverage files are produced
- PR #505: Use .utcnow() rather than .now()
- PR #498: Add a section on autograding wisdom
- PR #495: Raise an error on iopub timeout
- PR #494: Write documentation on creating releases
- PR #493: Update nbgrader to be compatible with notebook version 4.2
- PR #492: Remove generate_hubapi_token from docs
- PR #490: Temporarily pin to notebook 4.1
- PR #489: Make sure next/prev buttons use correct base_url
- PR #486: Add new words to wordlist
- PR #485: Update README gif links after docs move into nbgrader
- PR #477: Create a conda recipe
- PR #473: More helpful default comment box message
- PR #470: Fix broken links
- PR #467: unpin jupyter-client
- PR #466: Create nbgrader quickstart command
- PR #465: Confirm no SSL when running jupyterhub
- PR #464: Speed up tests
- PR #461: Add more prominent links to demo
- PR #460: Test that other kernels work with nbgrader
- PR #458: Add summary and links to resources in docs
- PR #457: Update formgrader options to not conflict with the notebook
- PR #455: More docs
- PR #454: Simplify directory and notebook names
- PR #453: Merge user guide into a few files
- PR #452: Improve docs reliability
- PR #451: Execute documentation notebooks manually
- PR #449: Allow --assignment flag to be used with transfer apps
- PR #448: Add --no-execute flag to autogradeapp.py
- PR #447: Remove option to generate the hubapi token
- PR #446: Make sure perms are set correctly by nbgrader submit
- PR #445: Skip failures and log to file
- PR #444: Fix setup.py
- PR #443: Specify assignments and students in the config file
- PR #442: Fix build errors
- PR #430: Reintroduce flit-less setup.py
- PR #425: Enable 3.5 on travis.
- PR #421: Fix Contributor Guide link
- PR #414: Restructure user guide TOC and doc flow to support new users
- PR #413: Windows support
- PR #411: Add tests for https
- PR #409: Make a friendlier development install
- PR #408: Fix formgrader to use course directory
- PR #407: Add --no-metadata option to nbgrader assign
- PR #405: nbgrader release typo
- PR #402: Create a Contributor Guide in docs
- PR #397: Port formgrader to tornado
- PR #395: Specify root course directory
- PR #387: Use sys.executable to run suprocesses
- PR #386: Use relative imports
- PR #384: Rename the html directory to formgrader
- PR #381: Access notebook server of formgrader user

Thanks to the following contributors who submitted PRs or reported issues that were merged/closed for the 0.3.0 release:

- alchemyst
- Carreau
- ellisonbg
- ischurov
- jdfreder
- jhamrick
- jklymak
- joschu
- lgpage
- mandli
- mikebolt
- minrk
- olgabot
- sansary
- svurens
- vinaykola
- willingc

0.2.x
-----

0.2.2
~~~~~

Adds some improvements to the documentation and fixes a few small bugs:

- Add requests as a dependency
- Fix a bug where the "Create Assignment" extension was not rendering correctly in Safari
- Fix a bug in the "Assignment List" extension when assignment names had periods in them
- Fix integration with JupyterHub when SSL is enabled
- Fix a bug with computing checksums of cells that contain UTF-8 characters under Python 2

0.2.1
~~~~~

Fixes a few small bugs in v0.2.0:

- Make sure checksums can be computed from cells containing unicode characters
- Fixes a bug where nbgrader autograde would crash if there were any cells with blank grade ids that weren't actually marked as nbgrader cells (e.g. weren't tests or read-only or answers)
- Fix a few bugs that prevented postgres from being used as the database for nbgrader

0.2.0
~~~~~

Version 0.2.0 of nbgrader primarily adds support for version 4.0 of the Jupyter notebook and associated project after The Big Split. The full list of major changes are:

- Jupyter notebook 4.0 support
- Make it possible to run the formgrader inside a Docker container
- Make course_id a requirement in the transfer apps (list, release, fetch, submit, collect)
- Add a new assignment list extension which allows students to list, fetch, validate, and submit assignments from the notebook dashboard interface
- Auto-resize text boxes when giving feedback in the formgrader
- Deprecate the BasicConfig and NbGraderConfig classes in favor of a NbGrader class

Thanks to the following contributors who submitted PRs or reported issues that were merged/closed for the 0.2.0 release:

- alope107
- Carreau
- ellisonbg
- jhamrick
- svurens

0.1.0
-----

I'm happy to announce that the first version of nbgrader has (finally) been released! nbgrader is a tool that I've been working on for a little over a year now which provides a suite of tools for creating, releasing, and grading assignments in the Jupyter notebook. So far, nbgrader has been used to grade assignments for the class I ran in the spring, as well as two classes that Brian Granger has taught.

If you have any questions, comments, suggestions, etc., please do open an issue on the bugtracker. This is still a very new tool, so I am sure there is a lot that can be improved upon!

Thanks so much to all of the people who have contributed to this release by reporting issues and/or submitting PRs:

- alope107
- Carreau
- ellachao
- ellisonbg
- ivanslapnicar
- jdfreder
- jhamrick
- jonathanmorgan
- lphk92
- redSlug
- smeylan
- suchow
- svurens
- tasilb
- willingc
