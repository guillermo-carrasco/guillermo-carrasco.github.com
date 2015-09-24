---
layout: post
title:  "Determining buffer size for RedisHandler in Python logbook"
date:   2013-10-02
comments: true
tags:
    - elasticsearch
    - logbook
    - logstash
    - matplotlib
    - python
---
A few weeks ago here in Stockholm we had a meetup about [Elasticsearch][elasticsearch]. In this
meetup they were talking about projects that use Elasticsearch, and one of these
projects was [Logstash][logstash]. Logstash is a tool for managing events and logs.
Basically, it collects your log events and store them into Elasticsearch. Later on,
with the provided web interface called Kibana, you can search within all your
logs in a really cool way.

I thought that this would be very useful for us and therefore I started to do some
testing. The tests worked so smoothly that we have decided to put Logstash into production,
and here comes the story. The figure below represents the recommended Lostash stack:

![Logstash architecture]({{ site.url }}/assets/images/determining-buffer-size-for-redishandler-in-python-logbook/getting-started-centralized-overview-diagram.png)

The message broker they recommend is Redis, and this is the one I tested.
The majority of our scripts and tools are written in Python, and for logging,
we’re using a logging package called [logbook][logbook]. If order to start sending
messages to Logstash in an easy way and less intrusively as possible, I decided
to implement a new log Handler for Redis, in such a way that to log into Logstash,
we will just have to add the new Handler to our Logger. If you don’t know that much about
python logging, take a quick look at [this][quickstart] page.

After implementing the first version of the handler, and pull-requested to the upstream
project, [Gustavo J.A.M Carnerio][gustavo], who has previously contributed to logbook,
suggested me to use buffering. What I was doing in my first implementation of the
handler was to push to Redis every single message that the handler emitted, directly.
I therefore implemented a buffer that is emptied when it reaches certain size,
or every second if never reaches that size, pushing the whole set of messages at once.
But… what size is optimal?

Actually, as Gustavo suggested the only way to determine the size for the buffer
is to run some tests and that’s what I did. To test the performance of the handler,
I prepared a [script][script] that for a set of buffer sizes, takes the time
required to insert a certain amount of messages. I tested different buffer sizes
and different amount of messages sent in a row. These are the results:

![Performance 1000000]({{ site.url }}/assets/images/determining-buffer-size-for-redishandler-in-python-logbook/performance_1000000.png)

If we zoom in, we can see that, in all cases, with a buffer of 128 messages we’ve
been able to insert more messages in less time. Buffering is indeed necessary,
otherwise it becomes really slow for higher number of events:

![Performance 100]({{ site.url }}/assets/images/determining-buffer-size-for-redishandler-in-python-logbook/performance_100.png)

![Performance 1000]({{ site.url }}/assets/images/determining-buffer-size-for-redishandler-in-python-logbook/performance_1000.png)

![Performance 10000]({{ site.url }}/assets/images/determining-buffer-size-for-redishandler-in-python-logbook/performance_10000.png)

![Performance 100000]({{ site.url }}/assets/images/determining-buffer-size-for-redishandler-in-python-logbook/performance_100000.png)

The speed-buffer size ratio seems stable throughout all tests but not all corner
cases are covered in this benchmark. Other factors like increasing or decreasing
the interval time for the automatic flushing (currently one sec., as said before),
can influence in the performance.

But at least these tests justify the default parameters (totally customisable, by the way),
of the RedisHandler in logbook.

Last but not least, thanks to Gustavo and Roman for the advices during the development
of the handler (you can see our discussions in the [pull request][pr] to the master project).


[elasticsearch]: http://www.elasticsearch.org/
[logstash]: http://logstash.net/
[logbook]: http://pythonhosted.org/Logbook/
[quickstart]: http://pythonhosted.org/Logbook/quickstart.html
[gustavo]: http://gjcarneiro.blogspot.se/
[script]: {{ site.url }}/assets/codes/determining-buffer-size-for-redishandler-in-python-logbook/redis_performance.py
[pr]: https://github.com/mitsuhiko/logbook/pull/92
