---
layout: post
title:  "Migrating my blog from WordPress to Jekyll + GitHub"
date:   2015-10-04
comments: true
tags:
    - others
    - programming
    - Jekyll
---

Yes, I also migrated my blog from hosted WordPress to the GitHub Pages + Jekyll combo.
This is a blog post about how and why I've done so, as well as some pointers on how
to do it yourself. There are lots of tutorials out there, so I won't enter into much detail on how to do X and Y.

Let's start with the most FAQ, _why?_

<!--more-->

##Why?

### Inspiration
People I professionally admire and respect decided a while ago to move their blogs from their previous
providers to this nice combo. The reasons vary, but basically having a blog you can deploy anywhere
and its not tight to a concrete provider is always a big win.

Have a look at [Brad Chapman][brad], [Roman Valls][roman] or [Robin Andeer's][robin] blogs, those are some
of the people I am talking about.

### Convenience
Its not a huge deal, but one problem that I often encountered with WordPress was that I could not edit
or write posts offline. This meant that whenever I was on a plane, or anywhere without a WiFi connection
and wanted to write a post, I had to do it on plain text for later copy pasting _and formatting_ in
WordPress editor.

This is over! I can now edit my posts in markdown and I **know** in advance how they are going to look.

### Too much money
WordPress is free, yes, _but_ you get adds in your posts and some space limitations. That didn't bother me
that much... until I bought my mussol.org domain. After paying for my domain, I discovered that I had to pay
to WordPress so that they allowed me to use it... whut? It was even more expensive than the cost of the
domain itself, and they didn't even removed the adds... bad WordPress, bad!

### Cool?...
Ok, I have to admit it, I feel cooler by writing posts in a simple text editor in markdown than using the
fancy WordPress editor page. Call me a hipster %-).

## How?

As I said, there are lots of How-To's for migrating from WordPress to GH + Jekyll, for example:

* [How-to: Migrating Blog from WordPress to Jekyll, and Host on Github](http://www.girliemac.com/blog/2013/12/27/wordpress-to-jekyll/)
* [Lessons Learned Switching From Wordpress On Dreamhost To Jekyll On GitHub](http://www.leemunroe.com/moving-wordpress-dreamhost-to-jekyll-github/)

**Create a skeleton with Jekyll**

Easy peasy, just type `jekyll new <name_of_your_blog>` and you already have a working blank blog.

Otherwise, just fork any of the thousand blog templates out there and work from that. I am actually
using my own flavor of [QckTheme](http://jekyllthemes.org/themes/qck-theme/).


**Discussions and comments**

Comments and discussions is a feature I didn't want to loose. After some googling,
I decided to use the [disqus][disqus] platform. Its easy to use, easy to integrate
with Jekyll, and it does the work perfectly well.

To import your already existing comments and discussions from WordPress just
follow the [import instructions][import_instructions] provided by disqus. If you
have your own domain name, and you kept the permalink structure on the migration, then
everything should work. Disqus will create threads based on your old URLs. If you don't have your own domain name... well, good luck!

Porting of comments worked super smoothly for me, and I can see all the comments from my old posts in
my newly moved blog.

**Google analytics**
Another thing that made me hesitate  about migrating was WordPress stats
page. The stats page in WordPress is so nice and gives you a very nice report on
your blog statistics like: Visitors, views, likes, countries, clicks, etc.

To get at least some basic stats about my blog, I just decided to go for [Google analytics][google_analytics],
as it is free and easy to integrate. Like disqus, only adding a small
JS snippet in all pages you want to track is enough after signing in into Google
Analytics and linking your page. In this case though, you can't recover stats from
WordPress, which is a pity since I had stats from 2012. Not a big deal though.

## Summary
I think the trouble was worth it, it was a bit tedious to move all the posts, since I decided to port them
manually, both for reviewing and because all exporters I found converted my posts to ugly html instead of
markdown.

_Bonus_: Following the core idea of the blog "In automation we trust", this blog is automatically tested in [Travis-CI](https://travis-ci.org/guillermo-carrasco/guillermo-carrasco.github.com)

[disqus]: https://disqus.com/
[import_instructions]: https://help.disqus.com/customer/portal/articles/466255-importing-comments-from-wordpress
[google_analytics]: http://www.google.com/analytics/
[brad]: http://bcb.io/
[roman]: http://blogs.nopcode.org/brainstorm/
[robin]: http://www.robinandeer.com/
