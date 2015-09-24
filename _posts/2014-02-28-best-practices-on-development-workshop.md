---
layout: post
title:  "Best Practices on Development Workshop"
date:   2014-02-28
comments: true
tags:
    - openscience
    - software quality
    - programming
---
Yesterday I held a workshop at [Science For Life Laboratory][scilife] (SciLife)
which I called "Best Practices on Development".

The aim of this workshop was to show the attendants (scientists on its majority)
how to develop software in a better way. On these years working on scientific environments,
I have seen quite a big tendency on not giving the deserved importance to software quality,
prioritizing only obtaining the desired results. This blog post from Chris Parr
describes [this][post] situation quite well.

<!--more-->

IMHO we are doing a good job in the production team at SciLife, all our code is
publicly available on GitHub, we have **some** of our software integrated in [Travis-CI](https://travis-ci.org/),
and we have a good collaborative workflow (Trello, Pull Requests, GH Issues, etc.).
For this reason, I decided that it would be good to share these good practices and
experience with the rest of the scientists at SciLife, as well as everyone who wanted to attend.

[Here][ws] you can find all the material of the workshop. On that repository, you can find:

* A lot of material on Git & GitHub, Python, styling, testing and debugging
* Two branches called exercises and solutions.
* The slides I used (which are not very informative as it was quite interactive :-P)

I tried to structure the workshop so that the people could solve this problem step by step:

> Is your first day, and they told you that you have to find a bug in a piece of
software, fix it, document it, and make sure that this doesn’t happen again (a.k.a write tests!)

The experience was awesome, people were very collaborative, even discovering some
non-intentioned bugs in my code due to last minutes changes (yep, practice what you preach…).
Even the mixture of background and levels, I am very satisfied about how the people
followed the workshop, all the effort put on it was definitely worth it.

Just hopping that this derives on a better development.

And needless to say, you’re free to re-use whatever you want from my repository!


[scilife]: http://www.scilifelab.se/
[post]: http://www.timeshighereducation.co.uk/news/save-your-work-give-software-engineers-a-career-track/2006431.article
[ws]: https://github.com/guillermo-carrasco/BestPracticesWorkshop
