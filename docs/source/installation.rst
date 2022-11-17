Installation and deployment
===========================

Installing a module
-------------------------
All modules follow the same installation steps.

1. Clone the relevant repository with ``git clone``.
2. Setup and activate the conda environment for the repository.
3. Download any relevant databases or external software that doesn't play nicely with conda.
4. Update the parameters.yaml file.
5. Test the module on the test data present in the GitHub repository.

Input/Output file structure
----------------------
Each module consists of a comma-delimited input and output file structured in the same way, such that it can be fed easily into downstream modules without modification. At minimum, it must contain the paths to all relevant input files, like raw short reads, assembled metagenomic contigs, etc. 

For example, for the short-read quality control pipeline, the input file looks like:

.. list-table:: Input file
   :widths: 25 25 50
   :header-rows: 1

   * - SampleID
     - Short-read-R1
     - Short-read-R2
   * - sampledata1
     - /path/to/sampledata1-r1
     - /path/to/sampledata1-r2
   * - sampledata2
     - /path/to/sampledata2-r1
     - /path/to/sampledata2-r2

And the output file looks like:

.. list-table:: Output file
   :widths: 25 25 50
   :header-rows: 1

   * - SampleID
     - Short-read-R1
     - Short-read-R2
   * - sampledata1
     - /path/to/sampledata1-quality-controlled-r1
     - /path/to/sampledata1-quality-controlled-r2
   * - sampledata2
     - /path/to/sampledata2-quality-controlled-r1
     - /path/to/sampledata2-quality-controlled-r2

This output file can be used as input for a number of downstream modules, like assembly or taxonomic profiling.

Running a module
-----------------

You can run each module in two ways, either at the command line or in on a slurm cluster. For details on slurm cluster deployment, see each of the READMEs. 

The command-line implementation derives from a custom command-line we built with Python's click interface. An example command deployment looks like:

::

  python /path/to/short-read-taxonomy.py -s /path/to/Snakemake/file -d outputdirectory --cores number_of_threads


