---
layout: post
title:  "Collecting disk usage metrics and plotting with Python"
date:   2013-06-01
---

Sometimes, when doing performance tests, you cannot avoid having to take some low-level system metrics.

I’m doing some tests of a Hadoop based genome sequence aligner called [Seal][seal].
I’m comparing the performance (just timing by now) against the most widely used sequence aligner, [BWA][BWA].
To do the tests I’m using different cluster configurations, so I can see when it is worth the use of
Hadoop in terms of types of nodes, amount of data, etc.

For one of these tests, which cluster configuration was just 2 (quite powerful) datanodes,
it has happened that BWA, using all 24 CPUs of the node, has been way faster than Seal
using both datanodes (4h vs 42 min aprox). Ok, I did expect that BWA performance would
be better in this case, as the overhead of managing all Hadoop processes, I/O in HDSF, etc,
would kill Seal performance. But… that difference?

I contacted with the IT staff of the HPC where I’m running my tests, and they immediately
sent back to me some system usage reports (awesome guys!). Now… I could have used a
spreadsheet to make some plots and analyze the data but, let’s be honest:

* In that case is ok, I don’t have that much data, but if you need to plot metrics
from very large files, a spreadsheet is just not an option.
* Copy & paste the data, make the plots, labels, etc… for each file, when I may have hundreds of files? NO, thanks.
* Booooriing… ;-)

So I thought that this would be a good opportunity to learn a bit of how to plot data using Python.
And [here][notebook] you can see the result. I’ve used a fraction of the disk usage metrics file, enough to illustrate the case.
By the way, the problem here was that the datanodes are intensively using the disks:
The mapreduce daemons writing the logs, and the TaskTrackers reading and writing from HDFS
(with the replication controll that this implies), everything on the same disk, makes this configuration I/O bounded.
You can see 4 picks of intense I/O in the graphics on the notebook, corresponding to the different analysis.
I try to make my posts in such a way that anyone can reproduce them,
so in my [GitHub][GitHub] you can find the ipython notebook and the disk metrics file.

[seal]:     http://biodoop-seal.sourceforge.net/index.html
[BWA]:      http://bio-bwa.sourceforge.net
[notebook]:  http://nbviewer.ipython.org/urls/raw.github.com/guillermo-carrasco/mussolblog/master/Collecting_disk_usage_metrics_and_plotting_them_with_python/Collecting_metrics_of_disk_usage_with_SAR.ipynb
[GitHub]:   https://github.com/guillermo-carrasco/mussolblog/tree/master/Collecting_disk_usage_metrics_and_plotting_them_with_python
