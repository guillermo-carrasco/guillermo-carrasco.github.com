---
layout: post
title:  "AWS Summit Stockholm 2016"
date:   2016-05-04
comments: true
tags:
    - AWS
    - cloud
    - scalability
---

![AWS kaynote](/images/aws-summit/keynote.jpg)

Today I attended the [AWS Summit Stockholm 2016][summit]. I wanted to attend last year but I was not
fast enough and couldn't get a spot. So this year I was thrilled!

I'll try to summarize the event in terms of my personal experience, since if I would describe every
talk, I would better redirect you to [AWS case studies][cases] page :wink:.

## Morning session

To begin with, at the entrance of the conference building, there was a woman DJ-ing. If you mix that
with the fact that it was 14º and sunny in Stockholm, you start the day in a really good mood.

After the registration and some good coffee and sandwiches, I went to check out the stands. There
I found companies I knew like Splunk, GitHub or SuSE (yes, they still exist!), but also unknown ones
for me, which was nice! More of that on the [stands](#stands) section.

The first talk in the schedule was from the Head of AWS Nordics & Baltics **Darren Mowry**. Before they
called him on stage, a video of a woman DJ-in was projected, together with loud music and inspirational
sentences... that was... strange :sweat_smile:.

Darren was talking about how the Nordics is one of the best places in the world for innovation and
technology, being the 4th largest startup market **in the world**.

After giving some more numbers, Ian Massingha, Chief Evangelist at AWS Europe came to stage. He gave
a 1h talk about all the services that AWS provide, and quite in detail to be honest. That may seem
like overwhelming, but if you have interest in the topic and you're new to AWS as I am, then you
can learn a lot from the talk.

Ian interviewed several people during the talk to expose how those people used AWS for their
companies. One of these people was **Johannes Löfgren**, head of DevOps at [iZettle][izettle], a Swedish
startup. He explained how AWS made their lives much more easier, since it is [PCI-DSS][pci] compliant,
which is a requirement if you work with credit card information.
Couldn't avoid thinking about the problem we have in academia, with human genetic data not being
able to be stored in cloud environment because of security/privacy and lack of regulation.

Last remark on the talk would be some tips and patterns for innovation from Ian. Those could be summarized
as:

1. Remove constrains: _Unbound creativity through technology_, don't waste your time building and
maintaining infrastructure, just focus on the product.
2. Observing and connecting: Observe and use your data, be a "data driven" company, listen to it!
3. Challenge the status quo: Don't go for a technology or architecture just because is "what people use".
Think about it and, if it doesn't fit your needs, innovate!

## Afternoon session
After a nice lunch and some more [stands](#stands), I went to the first talk in the startup track,
which was a bit disappointing. I was expecting an overview on the startup scene in the Nordics, and
what we got was a flood of numbers about investments done in the Nordics for the past few years, and
how the world is starting to know these countries as the new Silicon Valley.

I would have liked more a list of startups and success stories, but it was good anyway, and sort of
made me feel proud, even though I'm Spanish :blush:.

After that one I went to listen to the startup talks, which was more like what I wanted to listen to.

[Mojang][mojang] explained how they use AWS clusters to build users' Minecraft Realms. It was a
really interesting talk, and would love to have some of their slides to go over them in this post.

[QuizUp][quizup]'s talk was super interesting as well. It was more DevOps focused. They were
describing how all, absolutely all their infrastructure is defined as code. They use a Microservices
architecture as well and that makes it very easy to update simple services. A word of advice that I
through was good to consider was:

> Be careful with deployment when _all_ your infrastructure is defined as code. If you make too
many changes to the code, you'll spend a lot of time deploying. This will slow down the whole
system.

They do have policies for deployment other than "on every code change".

Last talk I attended was the _Deep Dive on Microservices and Amazon ECS_, given by **Johan Broman** -
Architect at AWS, and **Jude D'Souza** - Architect at [Wrapp][wrapp].

_Johan_ was talking about what a microservices architecture is and how it differs from the
traditional monolithic architecture. This architecture has several advantages over traditional ones,
like better maintainability, possibility of scaling only the demanded services, easier and faster
deployment, etc. However, it still has some disadvantages; service discovery is a problem, i.e
knowing which service is running where, using which port, etc. And services communication and
spawning as well.

_Jude_ came in a this point to explain the microservices architecture at Wrapp and how they've been
moving ahead. Jude described how they managed the aforementioned problems themselves with custom
solutions, and how [ECS][ecs] has solved _most_ of them (not all yet, service discovery is still a
problem).

Very interesting talk, this one!

## Stands
An important part of the conference was the companies stands/expos. As I said before, there were
some companies I've never heard about before in there, which was nice. A brief summary of the stands I
stopped by:

###### Github
Beside getting some awesome swag, I was talking with the guy at the stand. He was telling me how they
use AWS not only for their internal architecture, but also to host companies' GitHub Enterprise
instances in case that the company doesn't have or want to have GitHub in a local cluster. Pretty
neat.

###### Splunk
It was nice to talk with then, since I didn't have a clear idea of what Splunk is. If you've read my
[ELK post][ELK], then Splunk is pretty much like that, but hosted. Which is actually nice, since one of the things why we ended up _not_ using ELK at SciLifeLab, was because of its maintenance work.

Basically Splunk takes all the data from your logs and events and curates it for you so that you can
query it. Haven't tried it, but it is supposed to work with the majority of logging formats. Is that
even a finite set? I wonder :sweat_smile:.

###### Datadog
Yet another metrics platform, that one would be more like [Nagios][nagios]. If you've ever worked as,
or close to system administration/DevOps, you'd now about Nagios. Datadog is similar, but it monitors
not only server status but also _services_ status. Pretty nice life demo.

###### SuSE Linux
Still not very clear what they were doing there, to be honest. I stopped by because I used to work
with SuSE back in Barcelona, and got a bit nostalgic. I didn't know that they're still out there, and
even less doing business, good! They were explaining how they host some SuSE Enterprise instances in
AWS and how they prepare [AMIs][ami] for public use.

## Conclusion

I enjoyed the conference and learned quite a lot. Its a real pity that we in academia can't use this
kind of services yet for human data. I'd like to know what's the state of the art in this matter in
different countries, and how regulation is working there. Lots of problems like storage, scalability,
job scheduling, etc. could be palliated using platforms like AWS.

P.S: Bonus from the conference:

![Swag](/images/aws-summit/swag.jpg)

[summit]: https://aws.amazon.com/summits/stockholm
[cases]: https://aws.amazon.com/solutions/case-studies/
[elk]: http://mussol.org/2013/10/02/determining-buffer-size-for-redishandler-in-python-logbook/
[izettle]: https://www.izettle.com
[pci]: https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard
[mojang]: https://mojang.com/
[quizup]: https://www.quizup.com
[wrapp]: https://www.wrapp.com/
[ecs]: http://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html
[nagios]: https://www.nagios.com
[ami]: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html
