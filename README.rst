**NOTE** I started this from the fine Cookiecutter template, [cookiecutter-pylibrary](https://github.com/ionelmc/cookiecutter-pylibrary),
so the README and project has extra stuff in it that isn't working yet. Will trim down later and remove this note.

========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        |
        | |codeclimate|
    * - package
      - | |version| |downloads| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/citizens-climate-lobby-chicago-outreach/badge/?style=flat
    :target: https://readthedocs.org/projects/citizens-climate-lobby-chicago-outreach
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/hangtwenty/citizens-climate-lobby-chicago-outreach.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/hangtwenty/citizens-climate-lobby-chicago-outreach

.. |requires| image:: https://requires.io/github/hangtwenty/citizens-climate-lobby-chicago-outreach/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/hangtwenty/citizens-climate-lobby-chicago-outreach/requirements/?branch=master

.. |codeclimate| image:: https://codeclimate.com/github/hangtwenty/citizens-climate-lobby-chicago-outreach/badges/gpa.svg
   :target: https://codeclimate.com/github/hangtwenty/citizens-climate-lobby-chicago-outreach
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/ccl-chi-outreach.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/ccl-chi-outreach

.. |commits-since| image:: https://img.shields.io/github/commits-since/hangtwenty/citizens-climate-lobby-chicago-outreach/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/hangtwenty/citizens-climate-lobby-chicago-outreach/compare/v0.1.0...master

.. |downloads| image:: https://img.shields.io/pypi/dm/ccl-chi-outreach.svg
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/ccl-chi-outreach

.. |wheel| image:: https://img.shields.io/pypi/wheel/ccl-chi-outreach.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/ccl-chi-outreach

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/ccl-chi-outreach.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/ccl-chi-outreach

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/ccl-chi-outreach.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/ccl-chi-outreach


.. end-badges

Citizens' Climate Lobby Chicago chapters are doing a lot of outreach to small businesses in 2017. Here are helpers to
get a directory of contacts and keep track of our outreach efforts.

* Free software: BSD license

Installation
============

::

    pip install ccl-chi-outreach

Documentation
=============

https://citizens-climate-lobby-chicago-outreach.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
