---
layout: post
title:  "\"Mining\" twitter for my \"Twitteraniversary\""
date:   2014-09-26
comments: true
tags:
    - programming
    - analytics
    - bokeh
    - ipython
    - notebook
    - padnas
    - tweet
    - Twitteraniversary
    - tweeter
---
<center>
    ![Twitteraniversary]({{ site.url }}/assets/images/mining_twitter/aniversary.png)
</center>

So apparently today it has been three years since I created my twitter account, yay!
However I feel like it was just a year ago that I started using it seriously… maybe 2?
Was I using it before? I definitely think I had a "disconnection” period from twitter at some point…

I was asking myself these questions on the bus today, so I decided that it could be a
fun exercise to actually answer these questions with facts. How? Well, fortunately
you can pick up **all** the information you want from twitter using their complete [API][api],
and that’s what I did :-).

Just with a first call to the `/account/verify_credentials.json` API,
you already get a lot of information:

```json
{   "created_at": "Sun Sep 25 09:09:01 +0000 2011",
    "description": "Computer scientist. Passionate about new technologies, programming languages and geeky stuff in general. Very interested in bioinformatics.",
    "favourites_count": 37,
    "followers_count": 68,
    "friends_count": 72,
    "lang": "en",
    "listed_count": 2,
    "location": "Stockholm",
    "name": "Guillermo Carrasco",
    "screen_name": "guillemch",
    "status": {   "created_at": "Fri Sep 26 06:39:32 +0000 2014",
                  "favorite_count": 1,
                  "favorited": False,
                  "hashtags": ["Twitterversary"],
                  "id": 515390196389801984,
                  "lang": "en",
                  "retweeted": False,
                  "source": "Twitter for Android",
                  "text": "#Twitterversary it's 3 years in twitter today! (Only one using it actually xD)",
                  "truncated": False},
    "statuses_count": 376,
    "time_zone": "Stockholm",
    "utc_offset": 7200}
```

Isn’t it cool? One day like today in 2011 I created my account, and I already have some of the stuff I wanted:

* 37 favorited tweets
* 68 followers
* 376 tweets in total
* A mean of 0,34 tweets/day! You’ll not complain that I’m too verbose if you follow me…

This plot represents the number of tweets over time:

<center>
    ![Tweets per day]({{ site.url }}/assets/images/mining_twitter/tweets_per_day.png)
</center>

As I suspected… I was actually some time without tweeting anything: From February
24th 2012 to Aug 26th 2012. Not a year, but a couple of months.

I find interesting my tendency of not tweeting more that once per day. This is something
that I actually try to do consciously, I find annoying people that tweets too much
and floods your timeline. Yes okay, sometimes I can tweet 2, 3 or even go crazy an
throw 4 tweets per day, but not too often.

Now, we may want to be a bit more precise, right? For example this number, 376
tweets… how many are actually mine, and not retweeted? Twitter API documentation says:

> Retweets can be distinguished from typical Tweets by the existence of a retweeted_status attribute

So if we group the tweets by the field "retweeted_status” it turns out that only
173 tweets are mine! Thats slightly less than 50% of them. I think it’s ok, a good
balance between speaking and listening.

It is actually fun to play around with the Twitter API, you can keep answering silly
questions like the one before:

* What’s my most favorited tweet? 4 favorites, and it goes for the tweet for my
last blog post, so let’s see if I can improve it this time ;-)

<center>
<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr">Using celery to scale bioinformatics analysis <a href="http://t.co/dFM4cxcbCj">http://t.co/dFM4cxcbCj</a></p>&mdash; Guillermo Carrasco (@guillemch) <a href="https://twitter.com/guillemch/status/467283417076224000">May 16, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>

* What’s my most retweeted tweet? A tweet where I asked for help to Genomics people
on filling up a survey (that I still have to parse, shame on me!), with 8 retweets

<center>
<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr">Calling all <a href="https://twitter.com/hashtag/genomics?src=hash">#genomics</a> data wranglers! Please fill in this 10 mins survey about fetching &amp; updating ref data, thanks! <a href="https://t.co/tTz4qaCSwQ">https://t.co/tTz4qaCSwQ</a></p>&mdash; Guillermo Carrasco (@guillemch) <a href="https://twitter.com/guillemch/status/486172789456781312">July 7, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>

I think that you get the idea. I highly recommend you to play around with this,
it is quite fun! And you don’t have to code anything if you don’t want to, just
use the ipython notebook that I wrote for doing my analysis, either [raw code][code] or
the [final result][nviewer]. There are lots of explanations about what I’m doing :-)

Hope you have fun, if you did, share!


[api]: https://dev.twitter.com/overview/api
[code]: https://github.com/guillermo-carrasco/mussolblog/tree/master/mining_twitter_for_my_twitteraniversary
[nviewer]: https://github.com/guillermo-carrasco/mussolblog/blob/master/mining_twitter_for_my_twitteraniversary/Mining_twittew_for_my_twitteraniversary.ipynb
