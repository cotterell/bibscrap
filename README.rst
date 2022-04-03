========
bibscrap
========

.. image:: https://img.shields.io/pypi/v/bibscrap?style=flat
   :target: https://pypi.org/project/bibscrap/
   :alt: PyPI version

.. image:: https://readthedocs.org/projects/bibscrap/badge/?version=latest
   :target: https://bibscrap.readthedocs.io/en/latest/
   :alt: bibscrap's documentation

.. image:: https://badges.gitter.im/bibscrap/community.svg
   :alt: Join the chat at https://gitter.im/bibscrap/community
   :target: https://gitter.im/bibscrap/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. image:: https://github.com/cotterell/bibscrap/actions/workflows/build.yml/badge.svg
   :target: https://github.com/cotterell/bibscrap/actions/workflows/build.yml
   :alt: Continuous integration

.. image:: https://codecov.io/gh/cotterell/bibscrap/branch/main/graph/badge.svg?token=TQQWS0OQ0E
   :target: https://codecov.io/gh/cotterell/bibscrap
   :alt: Code coverage

.. image:: https://img.shields.io/pypi/l/bibscrap.svg
   :target: https://github.com/cotterell/bibscrap/blob/master/LICENSE.rst
   :alt: License: MIT

.. image:: https://img.shields.io/badge/code%20style-black-161b22.svg
   :target: https://github.com/psf/black
   :alt: Code style: black

Overview
========

The **bibscrap** package provides semi-automated tools for systematic literature reviews.

Requirements
============

* Python 3.8+

Install
=======

To install Bibscrap, use one of the commands below:

.. table:: Bibscrap install commands
   :widths: auto

   ===============  ==========================================
   Package Manager  Install Command
   ===============  ==========================================
   |pip|_           ``pip install --pre bibscrap``
   |pipenv|_        ``pipenv install --pre bibscrap``
   |poetry|_        ``poetry add --allow-prerelease bibscrap``
   ===============  ==========================================

.. |pip| replace:: ``pip``
.. _pip: https://pip.pypa.io/en/stable/

.. |pipenv| replace:: ``pipenv``
.. _pipenv: https://pipenv.pypa.io/en/latest/

.. |poetry| replace:: ``poetry``
.. _poetry: https://python-poetry.org/

Documentation
=============

Documentation is available online at https://bibscrap.readthedocs.io/ and in the
``docs`` directory.

Contributors: Getting Started
=============================

To download the development version of **bibscrap** and install its dependencies
into a virtual environment, follow the instructions provided below::

  $ git clone https://github.com/cotterell/bibscrap.git
  $ cd bibscrap
  $ poetry install -E devtools -E docs

To activate the virtual environment, use the following command::

  $ poetry shell

If you are part of the **bibscrap** development team, then you should also
install the pre-commit hooks once your virtual environment is activated.
You only need to do this once. Here is the command::

  $ pre-commit install

Contributors
============

=====================  ==========================================================  ============
Contributor            GitHub                                                      Role
=====================  ==========================================================  ============
Aidan Killer           `@aikill <https://github.com/aikill>`_                      Developer
Jack Solomon           `@jbs26156 <https://github.com/jbs26156>`_                  Developer
Matthew Pooser         `@mpooser <https://github.com/mpooser>`_                    Developer
Michael E. Cotterell   `@mepcotterell <https://github.com/mepcotterell>`_          Maintainer
Mitchell Casleton      `@MitchellCasleton <https://github.com/MitchellCasleton>`_  Developer
My Nguyen              `@mynguyen0628 <https://github.com/mynguyen0628>`_          Developer
=====================  ==========================================================  ============
