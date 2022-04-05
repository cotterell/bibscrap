========
Overview
========

**Bibscrap** provides semi-automated tools for the creation of
:term:`systematic literature reviews <SLR>` (SLRs). The methodology used to find
and review the relevant research literature when writing an SLR is rigorous,
often affording hypothesis testing related to real research questions about the
literature; however, that rigor also means more work for SLR authors, especially
when it comes to data collection and unbiased filtering. Bibscrap is designed
to make doing that work as painless as possible.

Development Status
==================

This documentation was generated for Bibscrap |version|, which is still in its
**pre-alpha** development phase. This is the earliest stage of software development.
The project is still establishing its requirements, and it contains code that is not
yet feature-complete. For information about what this means for Bibscrap |version|,
please refer to :ref:`api:Versions` in the API documentation.

Initial development will eventually lead to Bibscrap 1.0.0, the first official
:term:`stable release <STABLE>`. The planned phases for initial development are
presented in :ref:`the diagram <dev_phases>` below.

.. graphviz::
   :name: dev_phases
   :align: center
   :caption: Planned Initial Development Phases

   digraph foo {
       center=true
       margin=0.1
       bgcolor="transparent"
       rankdir=LR
       edge [color=dimgray]
       node [shape=box, style=filled, color=lightgray, fillcolor="#E3E3CD", fontname="Roboto Medium", fontsize=10]
       prealpha [label="Pre-alpha\n0.1.x", color="#B42F32", fillcolor="#C3585B", fontcolor=white]
       prealpha -> "Alpha\n0.2.x" -> "Beta\n0.3.x" -> "Release Candidate\n0.4.x" -> "First Stable Release\n1.0.0";
   }

Once more information is known about the development plan for versions after
1.0.0, this section of the documentation will be updated to reflect that
plan.

Planned Tools
=============

.. table::
   :align: center

   ===============  ===================
   Tool             Module
   ===============  ===================
   Bibscrap Find    ``bibscrap.find``
   Bibscrap Fetch   ``bibscrap.fetch``
   Bibscrap Filter  ``bibscrap.filter``
   ===============  ===================

Command-Line Interface
======================

Bibscrap offers a command-line interface...

Available Commands
------------------
