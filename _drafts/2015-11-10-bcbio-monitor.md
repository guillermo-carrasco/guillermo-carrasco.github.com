---
layout: post
title:  "Building an analysis monitor for a genomics pipeline: Tracking remote analyses"
date: 2015-11-10
comments: true
tags:
    - bioinformatics
    - SSE
    - Data analysis
    - Software architecture
---

![monitor](../assets/images/bcbio-monitor/logo-letters.png)

A typical genomics data analysis lasts usually for several hours or even days, depending on the type
of analysis performed. One common problem with these kind of analysis is that sometimes its hard, or
inconvenient at least, to know the current status of the analysis being performed. In most occasions
it involves SSH-ing to remote machines, looking for logs and GREP-ing through them.

[bcbio-nextgen][bcbio] is a python toolkit providing best-practice pipelines for fully automated high
throughput sequencing analysis.

<!--more-->

# The problem
As mentioned before, tracking long-run analyses is not always easy on these kind of workflows, and bcbio-nextgen
is not an exception. When running an analysis, the only way to know what's the status of it is by looking
into the logs. Wouldn't it be nice, and more convenient, to have a simple frontend layer that displayed
the progress of the current analysis?

# The solution
That's precisely what [bcbio-monitor][monitor] does. Now, to build a frontend for such a piece of software
like **bcbio-nextgen**, there are a couple of architectural **decisions** one needs to make. The very first
question that came to my mind was:

## Coupled or decoupled?
Do you want the tracker to be tighten to the software its tracking, in the sense of _requiring_ it to
function? You may think that's the logical choice at first, but think about this: bcbio-nextgen, as many
complex analysis pipelines has a lot of dependencies and its tricky to install. Even given [all the facilities][installation]
that [Brad Chapman][brad] give us to install bcbio, still time and computational resources are needed
to install bcbio-nextgen. I thought that, to be a practical tool, the potential users should be able to
install the monitor real quick and start tracking analyses wherever they're running (which is generally
a remote HPC or Cloud environment).

Every programmer should know the [importance of good logging practices][logging] for any application, right? bcbio-nextgen
does this _really_ well. So I though that I could just use the information from the log that bcbio-nextgen
generates, instead of inserting tracking code in the pipeline itself. **This makes the monitor independent
from the pipeline**, making it possible to just read ongoing analyses log files to build a status graph,
or even read finished analyses logs to get a run summary.

## Updating the frontend... polling? nah..
Having decided to use the log, we need a way of updating the client application (the browser) on every pipeline
step. There are mainly two options:

### Client-Server communication through polling

### Server-Client communication through HTML5 SSE events



[bcbio]: https://bcbio-nextgen.readthedocs.org/en/latest/
[monitor]: https://github.com/guillermo-carrasco/bcbio-nextgen-monitor
[installation]: https://bcbio-nextgen.readthedocs.org/en/latest/contents/installation.html
[brad]: https://github.com/chapmanb
[logging]: http://www.nsprogrammer.com/2013/06/logging-to-disk-most-important-part-of.html
