.. _background:

Introduction
==================

Welcome to the CAMP, a home for the wayward analyst in these heavily automated times.

The core principles behind the CAMP
------------------------------
The very understandable aim of most bioinformatics software development has been to make it easy-to-use. This approach is great, and it has vastly democratized who can work with complicated datasets; gone are the days when a bioinformatician needs a computer science degree. Optimizing for ease-of-use has resulted in many, many 'one-click-pipelines" designed for straightforward implementation of bioinformatic workflows. These approaches string together many different pieces of software to allow a very straightforward approach for data analysis: install, provide path your raw files, hit go, and wait. These are great -- we in no way want to disparage the incredible work of prior folks, and ourselves have used and loved many of these pipelines on many a time.

However, by virtue of minimzing user-input, one-click pipelines inherently yield a series of challenges, most notably opaque and potentially inflexible parameters, a tenuous reliance on many complicated dependencies that, upon breaking, will disrupt the pipeline. For example, small analytic decisions can wildly change your results. How you compute differential abundance, for example can drastically change host-microbe associations. A one-click pipeline, by encouraging quick-and-easy use, may lead users to not fully appreciate the vast array of parameters hard-working software engineers have built.

The CAMP is meant as an alterative to one-click approaches. We built it on three core principles.

**1) One module, one job, one output**

Going from short reads to, say, binned Metagenome-Assembled-Genomes, requires many intermediate steps and file types. This means that, in a single pipeline if one software dependency breaks, if a given user has an incompatible system with just one underlying tool, if one bug pops up in the code, the whole thing can fall apart.

With the CAMP, each module executes a single analytic task and provides the user with fully flexible parameters. Most run multiple different pieces of software, encouraging comparisons in how, say, different taxonomic profilers can yield different results. 

Additionally, every module takes a standardized set of inputs and outputs, allowing them to be easily strung together. 

**2) A user experience designed for algorithmic understanding**

One of the first steps in using a module is manually setting the ``parameters.yaml`` file. While an extra bit of effort, this encourages the user to think about what they're running, instead of just pushing go. We've tried to walk the line between ease of use and encouraging understanding of the underlying process.

As part of this, we are going to be implementing extremely substantive documentation for each module. Every README will, upon release of the full CAMP, have a "Theory" section that describes how the algorithms implemented at a certain section work. Ideally, the CAMP should equate to a semester long course in metagenomic analysis, with enough rich detail to take someone with minimal command-line experience all the way to a competent analyst.

**3) Highly flexible development**

Who are we to presume what your needs are, bioinformatically speaking. By separating tasks into modules, we've aimed to generate a toolkit that is maximally flexible. Further, if you need to build something else, constructing a new module based on existing pieces of software takes only a couple of hours for an experienced developer. This is in large-part due to our automated module-structure generation that every repository uses. Once you understand how one module is put together, you understand them all.

Distributed software maintenence
--------------------------------------

One of the most popular book genres in software engineering tackesl "dealing with legacy code." It's really difficult to work with other folks' code, no matter how good it is. Many pipelines and pieces of software have met an early end due to a graduating PhD student or a postdoc leaving for a new position. 

Our aim is to make the CAMP the home to the most cutting-edge, wild pieces of bioinformatic software being written out there. As a result, no one single person could possibly maintain everything. However, this is a good thing, as it's encouraged us to target "distributed development" within our standardized module framework.

By virtue of being part of the MetaSUB consortium, which spans 100 cities and 30 countries, we have been able to assign multiple owners and testers for each module with a clear chain of command and development strategy that spans the entire team. We can easily onboard new members due to the straightforward structure of the code, and if someone leaves, that person can deputize another to step up and take over management of a given module.

With distributed development, the CAMP will long outlive any one person -- or even institution.

Module structure -- how we write code
--------------------------------------

Our modules are designed to be simple. They contain software packages, some developed by us, others developed by third parties (please cite the references when needed!). 

We use Snakemake as our software wrapper.

<@LAUREN CAN YOU POPULATE?>
