================
Intervaltree-Bio
================

Convenience classes for loading UCSC genomic annotation records into a set of `interval tree <https://pypi.python.org/pypi/intervaltree>`__ data structures.

Installation
------------

The easiest way to install most Python packages is via ``easy_install`` or ``pip``::

    $ pip install intervaltree-bio

The package requires the ``intervaltree`` package (which is normally installed automatically when using ``pip`` or ``easy_install``).

Usage
--------

One of the major uses for Interval tree data structures is in bioinformatics, where the
intervals correspond to genes or other features of the genome.

As genomes typically consist of a set of *chromosomes*, a separate interval tree for each
chromosome has to be maintained. Thus, rather than using an single interval tree, you would typically use
something like ``defaultdict(IntervalTree)`` to index data of genomic features.
The module ``intervaltree_bio`` offers a ``GenomeIntervalTree`` data structure, which is a similar convenience
data structure. In addition to specific methods for working with genomic intervals it also
provides facilities for reading BED files and the refGene table from `UCSC <http://genome.ucsc.edu/>`__.

The core example is loading the transcription regions of the ``knownGene`` table from the UCSC website::

    >> from intervaltree_bio import GenomeIntervalTree
    >> knownGene = GenomeIntervalTree.from_table()
    >> len(knownGene)

It is then possible to use the data structure to search known genes within given intervals::

    >> result = knownGene[b'chr1'].search(100000, 138529)
    
It is possible to load other UCSC tables besides ``knownGene`` or specify custom URL or file to read the table from.
Consult the docstring of the ``GenomeIntervalTree.from_table`` method for more details.

Copyright
----------

  * Copyright (c) Konstantin Tretyakov
  * MIT license.
  * Report issues via `Github <https://github.com/konstantint/intervaltree-bio>`__.
