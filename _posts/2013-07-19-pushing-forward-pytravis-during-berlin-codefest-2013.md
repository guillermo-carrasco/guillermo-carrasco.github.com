---
layout: post
title:  "Pushing forward pytravis during Berlin Codefest 2013"
date:   2013-07-19
comments: true
tags:
    - programming
    - API
    - TDD
    - Travis-CI
    - Python
---
Today has been the second and last day of the [Codefest 2013][codefest2013]. Yesterday we were
working on an extension for [ipython-cluster-helper][ich], as I explained in my [previous post][pp].
Today, I’ve decided to push forward a small personal project that I started a few months ago.

Was around January when we decided in Science For Life Laboratory to integrate our development
in the Continuous Integration system [Travis-CI][travis]. Travis-CI is a freely hosted CI
system perfectly integrated with GitHub and with support for lots of programming languages.
It has been helping us a lot in our development process: Our genomics pipeline is being
automatically tested [there][bcbb-travis]. We develop mainly in Python, so I thought
that would be nice to programatically be able to check the status of our builds,
repositories, jobs, etc. So I decided to create a Python wrapper for the Travis-CI API.

I named this project **[pytravis][pytravis]**, and today I gave it a push. I had it a
bit abandoned due to other work with pressing deadlines, but today I brought it to a
quite mature state. At this moment, you can:

* Create python objects to represent: Users, repositories, builds, jobs, and logs
* List repositories by owner in a nice way very easily
* Get the state and other information of builds
* Access private API endpoints through GitHub API token authentication

I thought that one contribution like this could be very good for automating things,
as you don’t really need a browser to know the state of your projects. [Here][example] you have a
practical example of using pytravis on automated correction of programming exercices.

I hope it can be used by more people. It still needs development and features,
but I think is mature enough to start using it. Collaborations are welcome!


[codefest2013]: http://www.open-bio.org/wiki/Codefest_2013
[ich]: https://github.com/roryk/ipython-cluster-helper
[pp]: http://mussolblog.wordpress.com/2013/07/17/setting-up-a-testing-slurm-cluster/
[travis]: https://travis-ci.org/
[bcbb-travis]: https://travis-ci.org/guillermo-carrasco/bcbb
[pytravis]: https://github.com/guillermo-carrasco/pytravis
[example]: http://blogs.nopcode.org/brainstorm/2013/03/04/automated-python-education-via-unit-testing-and-travis-ci/
