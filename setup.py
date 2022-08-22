#!/usr/bin/env python

from setuptools import setup
import sys

sys.path.insert(0, '.')
from DistUtilsExtra import __version__ as pkgversion

LONG_DESCRIPTION = """
distutils-extra
===========================

**distutils-extra** can be used with python's distutils or the enhanced setuptools.


1. DISTUTILS
-------------------------

To make use of the distutils extenstions, you have to import the corresponding methods at the beginning of your setup.py:

.. code:: python

  from DistUtilsExtra.command import *

Furthermore you have to map the methods to the extended ones:

.. code:: python

  cmdclass = { "build" : build_extra.build_extra, "build_i18n" :  build_i18n.build_i18n }

If you have replaced the default build command by build_extra and defined the other commands e.g. build_i18n, the sub commands e.g. will be called automatically. There is no need to enable them in the setup.cfg anymore (This was require in a previous version). Disabling imported commands in the setup.cfg is still possible:

.. code:: bash

  [build]
  i18n=False

See the setup.cfg.example for a more complex layout.

Currently there are the following extensions available:

.. code:: bash

  build_extra: initiates the extensions
  build_i18n: provides gettext integration
  build_icons: installs icons
  build_help: installs a docbook based documentation

2. SETUPTOOLS
-------------------------

Just enable the corresponding build target in the setup.cfg:

.. code:: bash

  [build]
  i18n=True
  help=True
  icons=True

No further imports or modifications are required.

I hope that this code could help you to make your live easier,

3. DistUtilsExtra.auto
-------------------------

This module provides a setup() method for distutils and DistUtilsExtra which
infers as many setup() arguments as possible. The idea is that your setup.py
only needs to have the metadata and some tweaks for unusual files/paths, in a
"convention over configuration" paradigm.

This currently supports:

.. code:: bash

    - Python modules (./*.py, only in root directory)
    - Python packages (all directories with __init__.py)
    - GtkBuilder (*.ui)
    - Qt4 user interfaces (*.ui)
    - D-Bus (*.conf and *.service)
    - PolicyKit (*.policy.in)
    - Desktop files (*.desktop.in)
    - KDE4 notifications (*.notifyrc.in)
    - scripts (all in bin/, and ./<projectname>
    - Auxiliary data files (in data/*)
    - automatic po/POTFILES.in (with all source files which contain _())
    - automatic MANIFEST (everything except swap and backup files, *.pyc, and revision control)
    - manpages (*.[0-9])
    - files which should go into /etc (./etc/*, copied verbatim)
    - determining "requires" from import statements in source code
    - determining "provides" from shipped packages and modules

If you follow above conventions, then you don't need any po/POTFILES.in, ./setup.cfg or ./MANIFEST.in, and just need the project metadata (name, author, license, etc.) in ./setup.py.

----

Author: Henry Fuheng Wu, Sebastian Heinlein, Martin Pitt
"""

setup(
    name = 'distutils-extra-python',
    version = pkgversion,
    author = 'Henry Fuheng Wu, Sebastian Heinlein, Martin Pitt',
    author_email = 'wufuheng@gmail.com, sebi@glatzor.de, martin.pitt@ubuntu.com',
    description = 'Add support for i18n, documentation and icons to distutils',
    long_description = LONG_DESCRIPTION,
    packages = ['DistUtilsExtra', 'DistUtilsExtra.command'],
    license = 'GNU GPL',
    platforms = 'posix',
    entry_points = {"distutils.commands": [
           "build = DistUtilsExtra.command.build_extra:build",
           "build_i18n = DistUtilsExtra.command.build_i18n:build_i18n",
           "build_icons = DistUtilsExtra.command.build_icons:build_icons",
           "build_help = DistUtilsExtra.command.build_help:build_help",
           "clean_i18n = DistUtilsExtra.command.clean_i18n:clean_i18n",
           "pylint = DistUtilsExtra.command.pylint:pylint",
        ],},
)
