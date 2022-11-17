Developing for the CAMP
========================
Background
----------
Do you have an algorithm you want folks (a 30-country global consortium) to try? Do you see a module we need? If so, read on, and join the team.

We want to make the CAMP a home for the most cutting-edge bionformatic software out there. Doesn't matter if it's not microbial; if you want to try developing in our framework, you're more than welcome.

Connecting with the broader team
--------------------------------
First, if you'd like to meet the broader team, you're welcome to join the MetaSUB consortium for one of our monthly meetings, the times of which are listed here (https://metasub.org/). The bioinformatics subgroup meets immediately following the main meeting for 30 minutes. 

If you're rather reach out by email, please write  b <>  t <>  t <>  4  <> 0  <>  0 <> 1  at med dot cornell dot edu.

If you have specific suggestions or questions relevant to a module, please comment in the Issues section of its GitHub repository.

Module extension 
----------------

If you want to fork a module and extend it yourself, read on.

This module was partially envisioned as a dependable, prepackaged sandbox for developers to test their shiny new tools in. 

These instructions are meant for developers who have made a tool and want to integrate or demo its functionality as part of the standard {{ cookiecutter.module_name }} workflow, or developers who want to integrate an existing tool. 

1. Write a module rule that wraps your tool and integrates its input and output into the pipeline. 
    - This is a great `Snakemake tutorial <https://bluegenes.github.io/hpc-snakemake-tips/>`_ for writing basic Snakemake rules.
    - If you're adding new tools from an existing YAML, use ``conda env update --file configs/conda/existing.yaml --prune``.
    - If you're using external scripts and resource files that i) cannot easily be integrated into either `utils.py` or `parameters.yaml`, and ii) are not as large as databases that would justify an externally stored download, add them to ``workflow/ext/`` or ``workflow/ext/scripts/`` and use ``rule external_rule`` as a template to wrap them. 
2. Update the ``make_config`` in ``workflow/Snakefile`` rule to check for your tool's output files. Update ``samples.csv`` to document its output if downstream modules/tools are meant to ingest it. 
    - If you plan to integrate multiple tools into the module that serve the same purpose but with different input or output requirements (ex. for alignment, Minimap2 for Nanopore reads vs. Bowtie2 for Illumina reads), you can toggle between these different 'streams' by setting the final files expected by ``make_config`` using the example function ``workflow_mode``.
    - Update the description of the ``samples.csv`` input fields in the CLI script ``workflow/{{ cookiecutter.module_slug }}.py``. 
3. If applicable, update the default conda config using ``conda env export > config/conda/{{ cookiecutter.module_slug }}.yaml`` with your tool and its dependencies. 
    - If there are dependency conflicts, make a new conda YAML under ``configs/conda`` and specify its usage in specific rules using the ``conda`` option (see ``first_rule`` for an example).
4. Add your tool's installation and running instructions to the module documentation and (if applicable) add the repo to your `Read the Docs account <https://readthedocs.org/>`_ + turn on the Read the Docs service hook.
5. Run the pipeline once through to make sure everything works using the test data in ``test_data/`` if appropriate, or your own appropriately-sized test data. Then, generate unit tests to ensure that others can sanity-check their installations.
    * Note: Python functions imported from ``utils.py`` into ``Snakefile`` should be debugged on the command-line first before being added to a rule because Snakemake doesn't port standard output/error well when using ``run:``.
```

    python /path/to/camp_mag_qc/workflow/module_name.py --unit_test \
        -d /path/to/work/dir \
        -s /path/to/samples.csv
```
6. Increment the version number of the modular pipeline.
```

    bump2version --allow-dirty --commit --tag major workflow/__init__.py \
                 --current-version A.C.E --new-version B.D.F
```
7. If you want your tool integrated into the main CAP2/CAMP pipeline, send a pull request and we'll have a look at it ASAP! 
    - Please make it clear what your tool intends to do by including a summary in the commit/pull request (ex. "Release X.Y.Z: Integration of tool A, which does B to C and outputs D").




