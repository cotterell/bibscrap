=================
Sphinx Extensions
=================

The documentation site utilizes some custom Sphinx extensions that are stored in
the project's ``docs/_ext`` directory.

bibscrap.spinx.acmref
=====================

.. admonition:: Planning Phase
   :class: danger alert

   The contents of this module are still in the planning phase.

Introduction
------------

.. automodule:: bibscrap.sphinx.acmref
   :members:

Installation
------------

To install the ``bibscrap.sphinx.acmref`` Sphinx extension, carefully modify
your Sphinx project's ``conf.py`` to include Bibscrap's ``docs/_ext`` directory
(or a copy of it) in ``sys.path`` (see `here <sphinx_extensions_where>`__),
then add ``bibscrap.sphinx.acmref`` to your project's list of Sphinx extensions:

.. code:: python

   extensions = ["bibscrap.sphinx.acmref"]

.. |sphinx_extensions_where| replace:: Where to put your own extensions?
.. _sphinx_extensions_where: https://www.sphinx-doc.org/en/master/usage/extensions/index.html#where-to-put-your-own-extensions
