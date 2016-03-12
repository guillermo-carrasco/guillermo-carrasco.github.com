---
layout: post
title:  "NGS Data Processing Hackathon in Sofia, Bulgaria"
date:   2014-03-02
comments: true
tags:
    - openscience
    - hackathon
---
![Hackathon](/images/ngs_data_processing_hackathon/hackathon.jpg)

> A **hackathon** (also known as a hack day, hackfest or codefest) is an event in
which computer programmers and others involved in software development, including
graphic designers, interface designers and project managers, collaborate intensively
on software projects – Wikipedia

<!--more-->

On the past two days, a hackathon in Next Generation Data Processing has been
celebrated in Sofia, Bulgaria. The aim of this hackathon was to put together NGS Data
Processing projects developers and try to give a push to that projects in two days
of intense coding. Hackathons like this are a very good opportunity to know not
only cutting edge bioinformatics projects, but also the amazing people behind them.

Me, together with [Roman Valls][roman], have been working on a project called [FACS][facs],
witch stands for _Fast and Accurate Classification of Sequences_. Like the widely used
[fastq_screen][fastq_screen], FACS is a sequence classifier that tells you if a determined sequence
read belongs to a reference organism or not, so it can be used as a contamination checking tool.

The advantage of FACS over fastq_screen is that it uses a completely different algorithm, [bloom filters][bloom].
As it does not require an alignment step, it is faster than fastq_screen.
A previous version of FACS, written in perl, was [published][published] some time ago.
We are now working on a new C implementation. For this hackathon we planned to work on three main tasks:

1. Work on the automation of a complete test suite for testing and benchmarking FACS and fastq_screen,
**on a reproducible way**.

2. Fix the memory leaks reported by [Coverity Scan][coverty].

3. Implement paired-end support for FACS

So far, in two days we could work on tasks 1 and 2. There was already an automated
test suite, but there was a problem while automating the testing of fastq_screen using
the aligner bowtie2, because the indexes are not available in the public [Galaxy server][galaxy],
where all the reference data for the tests is downloaded, so if the user wouldn’t have then,
the benchmarking would crash. We implemented a simple method to build the indexes in case of not finding them.

After that last fix and a bit of refactoring in the tests, running "make benchmark"
on FACS root directory will build FACS, download reference data, generate test data with
[SimNGS][simngs], and run tests against this data with both FACS and fastq_screen
(which will be also automatically be downloaded and installed). If you have an
instance of CouchDB, the tests results will be uploaded to that instance, within
databases named _facs_ and _fastq\_screen_, in JSON documents like this one:

```json
{
   "_id": "6454e0822e48c768b02b036a4472690c",
   "_rev": "1-a9730c20e82fc579e912ff78290f6985",
   "contamination_rate": 0.333,
   "memory_usage": [
       25.18359375,
       47.51953125,
       47.53515625
   ],
   "p_value": 0.9999885,
   "total_read_count": 9000,
   "contaminated_reads": 2997,
   "sample": "facs/tests/data/synthetic_fastq/simngs.mixed_eschColi_K12_dm3_3000vs6000.fastq",
   "threads": 16,
   "bloom_filter": "facs/tests/data/bloom/eschColi_K12.bloom",
   "total_hits": 252986,
   "begin_timestamp": "2014-04-02T19:54:17.217+0200",
   "end_timestamp": "2014-04-02T19:54:17.245+0200"
}
```

You can use this information later for plotting the benchmarking results. We also
have an [IPython][ipython] notebook (**WIP**) for doing that, mostly work of Roman.
We already have plots for accuracy and speed. Our intention for the near future
is to provide a benchmarking and comparison of memory usage. We are using
[memory_profiler][mem_prof] for this.

On fixing memory leaks, we have to thank [Ognyan Kulev][ognyan] for his collaboration.
He helped us fix some problems and his knowladge on C was very useful for the task. There is still work to do though.

We finally couldn’t work on implementing paired-end reads support for FACS, but collaborations are welcome! :-)

Overall it has been a great experience, as always on this events I’ve learnt a lot
and heard about awesome projects going around. If you find this interesting, take a
look at [all the tasks][tasks] proposed for the hackathon and navigate through the related projects.

Hope you enjoyed the read!



[roman]: http://blogs.nopcode.org/brainstorm
[facs]: https://github.com/SciLifeLab/facs
[fastq_screen]: http://www.bioinformatics.babraham.ac.uk/projects/fastq_screen/
[bloom]: http://en.wikipedia.org/wiki/Bloom_filter
[published]: http://facs.scilifelab.se/
[coverty]: https://scan.coverity.com/projects/1599
[galaxy]: https://wiki.galaxyproject.org/Admin/DataIntegration
[simngs]: https://www.ebi.ac.uk/goldman-srv/simNGS/
[ipython]: https://github.com/SciLifeLab/facs/blob/master/facs/utils/benchmarks_facs.ipynb
[mem_prof]: https://github.com/fabianp/memory_profiler
[ognyan]: https://github.com/okulev
[tasks]: http://seqahead.cs.tu-dortmund.de/meetings:seqahead.hackathon4.tasks
