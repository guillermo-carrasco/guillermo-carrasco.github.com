---
layout: post
title:  "CodeFest and BOSC 2015 – Lots of workflows and Docker"
date:   2015-07-11
comments: true
tags:
    - bioinformatics
    - bosc2015
    - commonwl
    - docker
---
![Codefest 2015]({{ site.url }}/assets/images/bosc2015/codefest2015.jpg)

This year’s [BOSC][bosc] is being celebrated in Dublin, Ireland. For the third year in
a row I am attending to my favourite conference, and as usual, to the 2-days previous Hackathon or [Codefest][Codefest].

Starting by the hackathon, fantastic organization as always, thanks to [Curoverse][curoverse]
and [Bina][bina] for sponsoring and providing food and coffee (essential for working, well known fact).
There were as usual several projects going on, but this year I was greatly surprised by the size
of the [Common Workflow Language][cwl] group; all the people in the header picture are working on this project.
I got involved in the project as well – _actually had interest on it before, but couldn’t see how to contribute to it_.

<!--more-->

To start with I should try to explain what the project is about; citing the documentation:

>The Common Workflow Language (CWL) is an informal, multi-vendor working group consisting
of various organizations and individuals that have an interest in portability of data analysis workflows.
Our goal is to create specifications that enable data scientists to describe analysis
tools and workflows that are powerful, easy to use, portable, and support reproducibility.

> CWL builds on technologies such as [JSON-LD][jsonld] and [Avro][avro] for data modeling and [Docker][docker]
for portable runtime environments.

>CWL is designed to express workflows for data-intensive science, such as Bioinformatics, Chemistry, Physics, and Astronomy.

Basically, CWL tries to define a standard way of writing workflows, so that later different platforms,
i.e Radix or Arvados, can write implementations for it. The main idea is to create portable
and reproducible workflows. CWL is a project that was born on the previous hackathon in
Boston last year, that’s a message for those that doesn’t have much faith on hackathons ;-)

During the hackathon, we tried to run some examples and we found that, when Docker was
listed as a requirement, the workflows were not running **on our MacOS** computers due to
how Docker runs on Mac — Docker is based on Linux containers and, as Mac is not Linux… to run
docker you need to use something like [boot2docker][boot2docker], which creates a lightweight Linux
VM that runs docker inside it and talks to the host OS, in this case Mac. Problem here is
that when within a workflow a tool runs in a Docker container, it creates intermediate files
that the host OS cannot see because the container file system is not the same than the host
file system, breaking the workflow. After pinpointing the problem we issued a [Pull Request][pr]
that was merged after some review by [Peter Amstutz][peter], one of the main CWL contributors,
making us (me, [Robin][robin], [Roman][roman] and [Sinisa][sinisa]) official CWL contributors, yay! So that was a profitable codefest for us.

About the conference itself, what to say; very interesting as always. I won’t make a detailed summary of the talks as I use to do for two reasons

1. Very updated and live "_what is happening_" information on twitter following the hashtag #BOSC2015
2. Thanks to Google, the talks are being recorded and will be soon available on the BOSC site (linked above)

The only remarkable think that I want to comment on is the great idea of asking questions
to the speakers using twitter, IMHO it created an open and very active participation… kudos to the organizers!

What I take home from this 4 days of coding and talks is… Well a lot of things,
but to begin with – my interest in CWL is growing and growing, and I really want to
understand the project better and get involved! Also, that I really have to catch up
on the Docker ecosystem, I think that I’ve heard the word Docker on every single talk during the conference.

Hope you enjoyed reading! I feel a CWL-specific post coming up soon ;-)

[bosc]: http://www.open-bio.org/wiki/BOSC_2015
[Codefest]: http://www.open-bio.org/wiki/Codefest_2015
[curoverse]: https://curoverse.com/
[bina]: http://www.bina.com/
[cwl]: http://common-workflow-language.github.io/
[jsonld]: http://json-ld.org/
[avro]: https://avro.apache.org/
[docker]: http://docker.com/
[boot2docker]: http://boot2docker.io/
[pr]: https://github.com/common-workflow-language/common-workflow-language/pull/81
[robin]: http://www.robinandeer.com/
[roman]: http://blogs.nopcode.org/brainstorm/
[sinisa]: https://github.com/sinisa88
[peter]: https://github.com/tetron
