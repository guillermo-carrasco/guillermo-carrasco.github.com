---
layout: post
title:  "Migrating my blog from WordPress to Jekyll + Github"
date:   2015-09-15
comments: true
tags:
    - others
    - programming
---

This is a blog post about how and why I've migrated my blog from WordPress to a
Jekyll-based blog using GitHub for hosting. Let's start with the most FAQ, _why?_

#Why?

### Inspiration
people I admire/inspiring me doing it

### Convenience
Write offline, run locally...

### Too much money
WordPress is free, but I paied my domain and then I had to pay more for WordPress
to allow me to use it...

# How?

### Create a skeleton with Jekyll
Easy peasy, just type `jekyll new <name_of_your_blog>` and you already have a working
blank blog.

Configs changed: permalink to pretty to match WordPress URL's, some CSS to make it
a bit of my own. Devel configuratio to load drafts and change base URL

Added redcarpet extension for markdown parsin github style

### Discussions and comments

Comments and discussions is another feature I didn't want to loose. After some googling,
I decided to use the [disqus][disqus] platform. Its easy to use, easier to integrate
with Jekyll, and it does the work perfectly well. I only needed to:

1. Create a disqus account
2. Copy the "universal code" (a piece of JavaScript)
3. Add the universal code to the post template, after the content, in a conditional
of the style `{% if page.comments %} <universal_code_here> {% endif %}`
4. On each post I want to allow comments, I add the directive `comments: true` on top.

And that's it, you get posts with comments :-)

Now, to import your already existing comments and discussions from WordPress just
follow the [import instructions][import_instructions] provided by disqus. If you
have your own domain name, and you kept the permalink structure on the migration,
everything should work. If you don't have your own domain name... well, good luck!

Porting of comments worked super smoothly for me. 

### Google analytics
One of the things that made me hesitate more about migrating was WordPress stats
page. The stats page in WordPress is so nice and gives you a very nice report on
your blog statistics like: Visitors, views, likes, countries, clicks, etc.

To get at least some basic stats about my blog, I just decided to go for [Google analytics][google_analytics],
as it is free and easy to integrate. Like disqus, only adding a small
JS snipped in all pages you want to track is enough after signing in into Google
Analytics and linking your page. In this case though, you can't recover stats from
WordPress, which is a pity since I had stats from 2012. Not a big deal though.

[disqus]: https://disqus.com/
[import_instructions]: https://help.disqus.com/customer/portal/articles/466255-importing-comments-from-wordpress
[google_analytics]: http://www.google.com/analytics/
