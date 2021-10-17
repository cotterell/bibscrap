======================
Bibscrap |version| API
======================

.. |semver| replace:: Semantic Versioning 2.0.0
.. _semver: https://semver.org/spec/v2.0.0.html

Definitions
===========

Throughout the Bibscrap |version| API documentation, capitalized key words
are used to signify various requirements related to the API specification.
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be
interpreted as described in :rfc:`2119`. Other capitalized key words that appear
in this documentation SHOULD be interpreted as defined below.

.. glossary::

   INITIAL DEVELOPMENT
   INITIAL DEVELOPMENT VERSION
       A Bibscrap version of the form ``0.Y.Z`` or ``0.Y.Z-alpha.N`` is an
       **initial development** version. An :term:`INITIAL DEVELOPMENT` version
       SHOULD NOT be considered :term:`STABLE` as it  MAY change at any time.

   PRE-RELEASE
   PRE-RELEASE VERSION
       A Bibscrap version of the form ``X.Y.Z-alpha.N`` where ``X >= 1``
       is a **pre-release** version of its associated version, ``X.Y.Z``, and
       MAY not satisfy the intended compatibility requirements described in the
       :ref:`api:Public API` of version ``X.Y.Z``. A :term:`PRE-RELEASE` version
       SHOULD NOT be considered :term:`STABLE`.

   STABLE
   STABLE VERSION
       A Bibscrap version of the form ``X.Y.Z`` is a **stable** version
       that meets the intended compatibility requirements described in its
       :ref:`api:Public API`.

Versions
========

The Bibscrap team makes every effort to use |semver|_. Given a Bibscrap version
number ``MAJOR.MINOR.PATCH[-alpha.PRE]``, its semantic components are ``MAJOR``,
``MINOR``, ``PATCH``, and ``PRE``. We only bump (i.e., increment) the semantic
components of a Bibscrap version under specific scenarios, as described in the
:ref:`table below <component_bump_scenarios>`.

.. table:: Semantic Version Components & Bump Scenarios
   :name: component_bump_scenarios

   =========  =================================================================
   Component  Bump Scenario
   =========  =================================================================
   ``MAJOR``  Incompatible :ref:`api:Public API` changes are introduced.
   ``MINOR``  New functionality is introduced in a backwards compatible manner.
   ``PATCH``  Backwards compatible bug fixes are introduced.
   ``PRE``    Changes are introduced to a :term:`PRE-RELEASE`.
   =========  =================================================================

When ``-alpha.PRE`` is present in a Bibscrap version number, it denotes a
:term:`PRE-RELEASE`. The Bibscrap team uses :term:`PRE-RELEASE` versions to
make some API changes, feature additions, and bug fixes available ahead of their
associated :term:`STABLE` or :term:`INITIAL DEVELOPMENT` versions.

When ``MAJOR`` is zero in a Bibscrap version (e.g., ``0.MINOR.PATCH[-alpha.PRE]``),
that denotes an :term:`INITIAL DEVELOPMENT` version, regardless of its ``MINOR``,
``PATCH``, and ``PRE`` values.

Public API
==========

.. rubric:: Changes

.. todo::

   After Bisbscrap 1.0.0 is released, all changes to the :ref:`api:Public API`
   will need to be be documented in order to comply with |semver|_.

bibscrap
--------

.. automodule:: bibscrap
   :members:

.. autodata:: bibscrap.__version__

bibscrap.core
-------------

.. automodule:: bibscrap.core
   :members:

bibscrap.core.event
-------------------

.. automodule:: bibscrap.core.event
   :members:

bibscrap.util
-------------

.. automodule:: bibscrap.util
   :members:

Internal API
============

bibscrap.cli
------------

.. automodule:: bibscrap.cli
   :members:


bibscrap.cli.app
----------------

.. automodule:: bibscrap.cli.app
   :members:

bibscrap.cli.commands
---------------------

.. automodule:: bibscrap.cli.commands
   :members:
