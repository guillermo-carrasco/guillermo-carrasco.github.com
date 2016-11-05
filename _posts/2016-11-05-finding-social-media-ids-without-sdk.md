---
layout: post
title:  "Finding user's social media IDs without an SDK"
date:   2016-11-05
comments: true
tags:
    - Fscebook
    - Twitter
    - Instagram
    - Social media
---

If you are a developer and work with social media, there is most surely a task you've faced. A simple
task that should be easy but requires either to set up an SDK with OAuth tokens and so on, or use
web services like [findmyfbid](http://findmyfbid.com/). Exactly, the task is as simple as finding a
_user id_ from a social media profile.

There are several reasons for what you would want to store this ID, being the main one its uniqueness.
Whatever the reason it is, maybe that is the only interaction you want with the social network in that
moment/service. If so, setting up SDKs with all the authentication process etc, may seem a bit like
"using a sledgehammer to crack a nut".

Inspecting the source code of the main social media profiles, i.e Facebook, Instagram and Twitter, I
realized that in all of then, the user ID is embedded in some part in the source code. All I had to do
is find a couple of regexes to mach those parts and.. voilà!

[social_ids][social_ids] is a package I wrote to help precisely
with this. No need to set SDKs, tokens or any configuration. You don't even need to write a line of
code if you don't want to, since it has a CLI. Install with `pip install social_ids`

**As CLI tool**

Quite simple:

```
~> socialid --help
Usage: socialid [OPTIONS] NETWORK HANDLER

Options:
  --help  Show this message and exit.
```

An example

```
~> socialid twitter guillemch
ID for twitter handler "guillemch" is: 379637011
```

**As a package to import in your code**

Simple as well

```python
# Import the networks you want
from social_ids.networks import facebook

# Then use the get_id method with the handler
_id = facebook.get_id('zuck')
```

**Networks**

Right now social_ids works with:

* Facebook
* Twitter
* Instagram

Of course [its open source][social_ids], tested, MIT licensed and released to PyPi. If you want to add a social network to it, feel
free to submit a Pull Request and I'll have a look :smile:.

Hope its useful for more people! If it was, I'd be happy if you share this post and give the project a star on
[GitHub][social_ids]. Or just enjoy it!


[social_ids]: https://github.com/guillermo-carrasco/social_ids
