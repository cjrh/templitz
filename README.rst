.. image:: https://travis-ci.org/cjrh/templitz.svg?branch=master
    :target: https://travis-ci.org/cjrh/templitz

.. image:: https://coveralls.io/repos/github/cjrh/templitz/badge.svg?branch=master
    :target: https://coveralls.io/github/cjrh/templitz?branch=master

.. image:: https://img.shields.io/pypi/pyversions/templitz.svg
    :target: https://pypi.python.org/pypi/templitz

.. image:: https://img.shields.io/github/tag/cjrh/templitz.svg
    :target: https://img.shields.io/github/tag/cjrh/templitz.svg

.. image:: https://img.shields.io/badge/install-pip%20install%20templitz-ff69b4.svg
    :target: https://img.shields.io/badge/install-pip%20install%20templitz-ff69b4.svg

.. image:: https://img.shields.io/pypi/v/templitz.svg
    :target: https://img.shields.io/pypi/v/templitz.svg

.. image:: https://img.shields.io/badge/calver-YYYY.MM.MINOR-22bfda.svg
    :target: http://calver.org/

**ALPHA**

templitz
========

File templates for faster project bootstrap

Overview
--------

So you're making another Python project and there are a bunch of
boilerplate files you need (use cookiecutter), **or** you have an
existing project that you want to add some stuff to (cookiecutter
doesn't help). ``templitz`` offers a very lightweight way to add
some typical files to a project.

For example:

.. code-block:: bash

   $ templitz -t travis
   $ templitz -t appveyor

These two commands will dump a typical ``.travis.yml`` and a
``appveyor.yml`` into your current directory (which should probably
be the root of a Python project for any of this to make sense).

This program does nothing other than look up a file with a ``.templitz``
extension, and if found, copies that into your target folder. It's just
an easy way to add standard, boilerplate files to projects. Examples
are CI configs, ``setup.py``, ``flit.ini``, ``README.rst``, ``pytest.ini``
and so on. This tools just does the same copy-from-a-previous-project
file copying that you would normally do by hand.

Here are a few more examples:

.. code-block:: bash

   $ templitz -t asyncio

This one dumps a typical starter ``main.py`` for an ``asyncio``-based
application.

How about a C/C++? This one will dump a generic ``Makefile`` that will
work out-of-the-box for most typical C/C++ projects:

.. code-block:: bash

   $ templitz -t Makefile

BYO templitz
------------

``templitz`` includes a few example templates (in the ``/library``
directory), but you can also add your own quite easily: just set
the ``TEMPLITZ_PATH`` env var to configure your own search path for
templates:

.. code-block:: bash

   $ export TEMPLITZ_PATH=$HOME/.mytemplitz:$HOME/.myothertemplitz

Then your own templitz will be found automatically. Note that the first
templit found that matches the given ``-t`` parameter is the one that
hits, and the ``TEMPLITZ_PATH`` setting is checked first.

Reference
---------

.. code-block:: bash

    $ templitz --help
    usage: templitz.py [-h] [-t TEMPLATE] [-i] [-l] [-s] [-o OUTDIR]
                       [-p PARAMS [PARAMS ...]]

    optional arguments:
      -h, --help            show this help message and exit
      -t TEMPLATE, --template TEMPLATE
      -i, --info            Information about the templit.
      -l, --list            List all available templitz.
      -s, --stdout          Write to stdout instead of file.
      -o OUTDIR, --outdir OUTDIR
                            Output directory.
      -p PARAMS [PARAMS ...], --params PARAMS [PARAMS ...]

