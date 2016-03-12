---
layout: post
title:  "PyCon Sweden – Day 2"
date:   2015-05-14
comments: true
tags:
    - python
    - pyconsweden
---
![Guillermo & Robin](/images/pycon/our_presentation.png)

Today was the second day of PyCon Sweden 2015, which marked the end of this fantastic conference.
After an excellent set of talks the first day, the expectations were high! I have to say though that,
given that I was giving a talk today together with Robin Andeer, I could not be as focused as yesterday.
Here is my best attempt on summarizing the talks I found more interesting.

<!--more-->

## 1. Keynote – <u>Kate Heddleston</u>

More about Kate [here][kate].

The title of the talk was "The ethics of being a programmer". Kate has given a wonderful talk about the situation of
privacy and freedom when it comes to the digital world, that at the end of the day, is the personal world as well.
The talk started with the story of how her father saves lives as a doctor. He has the **legal** and _moral_ obligation to do his absolute best to save these lives.

This could be extrapolated to us as developers as well, maybe we cannot directly save the life of one person that has had an accident, but we can reach thousands of people, and as Kate said "The power of reaching thousands of people comes with a responsibility and ethics".

The talk has gone around two "study cases": Twitter harassment and Snapchat pornography "sharing".  Unfortunately this is one of the talks where you _have to be there_ in order to really get what she was talking about.

**Very** nice discussion at the end of the talk, as every time that morality or ethics take place on a conversation (believe me, I’m a vegan…).

## 2. Why Django sucks – <u>Emil Stenstrom</u>

More about Emil [here][emil].

The talk started with a disclaimer that drew my attention:

> Is not that I hate Django, but I think its important to know its not-so-good parts as well, you can’t just love something blindly.

I think all developers will agree on this: how many times have you been involved in a discussion about lets say, frameworks, where the two parts were blindly defending their framework ignoring or playing down its defects? I have, both listening and blindly participating. I think we should sometimes just be more objective :).

The talk focused on three main problems that Emil finds in Django.

1. Shared templates: Rendering everything in JS is a bad practice, rendering everything server side as well. You need to find a balance and render/process a bit on both sides, and to do so you need to be able to process templates on both sides. Django does not have a good solution for this.

2. Server push: It is not possible with Django (at least out of the box) to sent notifications to the clients, its always the client the one that needs to send a request to the server to get any information. In order to build any efficient application that requires real time notifications (a chat, some kind of timeline, etc), you need to be able to do this.

3. Template components: In order to add an external widget to your application, for example, you need to modify lots of bits of code: Add the JS, add the CSS, and link to those (and place correctly) wherever you have to use them. It would be more convenient and cleaner that adding components was easier and more independent.

## 3. How Python Drives the Analysis of Billions of DNA Sequences – <u>Guillermo Carrasco and Robin Andeer</u>

More about me… nah, you’re already reading my blog. More about Robin [here][robin].

So that was our talk! I’ll let other judge the quality of the talk and I'll say only two things. One is that you can find _everything_ about our talk in [this repository][repo], from the slides to the transcript of what we said (maybe not 100% updated, but informative enough).

Second is about the feeling of the talk, which was great! Despite the jitters, the talk was relaxed and people seemed interested. We got some very interesting questions at the end of the talk, and even after the questions time, people came to us to congratulate us and/or continue the discussion, that was very reinforcing!

What to say… thank you very much :) It was great talking to everyone, and of course I am always open to discussions! Just leave a comment or send me a mail.


## 4.How to build a web application with Flask and Neo4j – <u>Nicole White</u>

More about Nicole [here][nicole_blog]. GitHub [here][nicole_gh].

This talk was my favourite of today. Not only because the topic was interesting (never saw a graph database in action before), but also because of the format of the presentation.

Nicole started describing a little bit the differences between a relational database and a graph database. As an example she used a very simple schema with users and posts, that then showed as a graph where the joint table disappeared in favour of just notes pointing to each other.

During the next part of the presentation Nicole followed the FlaskR tutorial but, instead of using SQLite, she used Neo4j. The coolest thing of the presentation is that she actually deployed the app in Heroku for us in the audience to sign up and publish posts. This was risky but payed off, as we could see real time how the database was being populated, and how the relations between the nodes of the graphs were being created. At the same time, Nicole was showing the important bits of code that did the work.

Amazing presentation, kudos to Nicole ^^

## Conclusions

Wrapping up two days of conference is difficult, but I hope that my summaries for these two days are enough to give you an idea of how interesting this has been and how much have I learned.

Just want to thank the conference staff and voluntaries for letting us talk and for an amazing organization: one of the very few conferences that I haven't starved for being vegan, fantastic!

Also thanks a lot to Robin for bearing with me before and during the presentation, we’ve worked hard on this together :)

Remember, share if you liked it! Thanks!

[robin]: http://www.robinandeer.com/
[kate]: https://kateheddleston.com/
[emil]: https://friendlybit.com/
[repo]: https://github.com/guillermo-carrasco/PyConSweden2015
[nicole_blog]: http://nicolewhite.github.io/
[nicole_gh]: https://github.com/nicolewhite
[flaskr]: http://flask.pocoo.org/docs/0.10/tutorial/introduction/
