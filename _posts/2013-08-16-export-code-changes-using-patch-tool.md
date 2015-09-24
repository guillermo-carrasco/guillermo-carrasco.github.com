---
layout: post
title:  "Export code changes using patch tool"
date:   2013-08-16
comments: true
tags:
    - programming
    - contribute
    - diff
    - patch
---
First of all, we all agree that Git, SVN, or any other Control Version System (CVS)
is the way of developing code, right? Far away are those days where developers mailed
zipped codes with unambiguous version numbers (everyone can see that software-v1-0.0.2.3.43
is an important update over software-v1-0.0.2.3.44, right?). We also know that it is
better to develop locally, and, after properly testing, push to production and deploy.

<!--more-->

However, there are still software that is not under CVS, or maybe you want to do a small
change and you don’t want to clone an entire repository, make the corresponding changes
and propose a merge (very easy to pull-request in GitHub, but a bit more tricky if the
repository is in a pure git server). It also may happen (actually, it happened
to me recently) that you’re happily developing in a server (you sometimes need to develop
server-side) and in the moment of pushing to the upstream repository, you discover that
you cannot: Oh, permission denied because GiHub doesn’t recognize my ssh-key, and I cannot
create a new one because the sys-admins doesn’t allow me (security policies).
Now… what can we do? Well, basically we have three options (sure, that there are more):

* ~~Manually copy all the changes, apply them in your local copy, and push to upstream~~:
Wait… I’ve been implementing this feature for days! I’ve made a lot of changes. No way.
* ~~SCP the whole repository to your local machine and push to upstream from there~~:
May work, but is not a good solution: Transferring the the whole repository to your
machine may be intense, user/permission errors, etc. And, what if you have some
local change in your copy? They will be overwritten.
* Make a diff patch.

> "**patch** is a Unix program that updates text files according to instructions contained
in a separate file, called a patch file. The patch file (also called a patch for short)
is a text file that consists of a list of differences and is produced by running the
related diff program with the original and updated file as arguments. Updating files
with patch is often referred to as applying the patch or simply patching the files – Wikipedia"

So there you have it. Actually, the output of the git diff command is all you need to create the patch, on the server repo:

```bash
$> git diff > my_changes.patch
```

And on the local copy:

```bash
$> cd repo
$> patch -p1 < my_changes.patch
```

This will apply the changes on every modified file to your local copy. [Here](http://jungels.net/articles/diff-patch-ten-minutes.html) you
have a great blog post about how to work with diff and patch.

As a side note, patch is the system used to propose fixes to, for example,
[Ubuntu software packages](http://packaging.ubuntu.com/html/patches-to-packages.html).
