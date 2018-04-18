---
layout: post
title:  "QCon AI 2018 - Thoughts and take aways"
date:   2018-04-10
comments: true
tags:
    - ai
    - machine learning
    - conference
---

Last week I attended [QCon AI][qcon] in San Francisco, CA. QCon AI is a branch of
QCon focusing on Machine Learning and AI and targeted to software engineers.

In this post I will briefly talk about some of the most interesting talks (for me, of course)
and general thoughts and take aways. Most of the conference slides have already been
uploaded to the [conference schedule page][qcon-schedule], and I imagine most of
the talks will eventually be uploaded into [QCon Youtube channel][youtube], so go
there for details if you're interested in a particular talk!
<!--more-->

### Opening keynote

The conference started with a keynote from Uber, Matt Ranney. Matt is a software
engineer working in the self-driving car division at Uber. The talk gave an overview
of how self-driving cars can help reduce accidents and save time. Specially for
Americans, who spend around 293 hours/day in a car! Matt also talked about how a self-driving
car works on global terms. He also explained with some level of detail the infrastructure
that Uber has for testing and releasing new versions of the cars.

It was a very interesting talk. And no, Matt did not talk about [the tragic accident][accident]
that happened a few weeks ago in Arizona.

### The conference

Another very interesting talk was given by Michael Manapat from stripe. The interesting
part about that talk was their approach on testing and improving a classification
model already deployed in production. If a model is already deployed, how do you
keep collecting data for future improvements? If it is already deployed, it is
already affecting the outcome. A particular example was detect fraudulent transactions.
If you take actions on those transactions, they're not gonna happen, and thus your
future dataset is going to be unbalanced and it is hard to measure the performance
of the current model. One thing you can do is to let slip a % of transactions classified
as fraudulent and see if they're actually fraudulent or not. In all the cases, save the
prediction and real outcome for testing.

There were many talks about frameworks and visualizations. TensorFlow was a reall star in
the conference, and the TensorFlow/[TPU][TPU] presentation by Magnus Hyttsten from
Google was simply amazing.

Interpretability was another hot topic, and there were many small talks about tools
and techniques to help to explain your models' results. That's something ML practitioners
don't think much about until the moment they have to explain the results to someone
that has never heard about ML before.

### Closing keynote

The conference closed with a very interesting and inspirational talk by Rachel Thomas.
Rachel talked about bias in ML and gave some examples. Specially in NLP, where
models have been trained with corpus of ordinary texts like emails, articles, etc.
Some examples given were black people being misclassified as gorillas, black people being
classified as more prone to relapse after being in prison or jobs like "housekeeping"
or "nurse" being more tightly associated with women, while words like "business" and "success"
being closer to the word man. This is a sign that our training
sets are biased, and is something that really matters. Big companies like Google
are [already taking an action][google].

#### Conclusion

Overall a very nice an inspirational conference. Very well organized and talks
were generally of high quality. I will definitely attend next year!


<!-- Links -->
[qcon]: https://qcon.ai
[qcon-schedule]: https://qcon.ai/schedule/qconai2018/tabular
[youtube]: https://www.youtube.com/channel/UCLI_iq5wEySHTOb7xk2F7Ww
[accident]: https://www.theguardian.com/technology/2018/mar/19/uber-self-driving-car-kills-woman-arizona-tempe
[TPU]: https://cloud.google.com/blog/big-data/2017/05/an-in-depth-look-at-googles-first-tensor-processing-unit-tpu
[google]: https://developers.googleblog.com/2018/04/text-embedding-models-contain-bias.html
