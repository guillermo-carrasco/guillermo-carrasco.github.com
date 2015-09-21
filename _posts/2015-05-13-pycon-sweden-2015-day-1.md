---
layout: post
title:  "PyCon Sweden 2015 – Day 1"
date:   2015-05-13
comments: true
tags:
    - python
    - pyconsweden
---
Today was the first day of PyCon Sweden 2015. I’ve had the luck of attending for the first time!
And this means that I’ve attended to 50% of all PyCon Sweden editions! (yes, its only its second year.. :-P ).
Joking apart, even though its a young fork of the main PyCon conference, here in Sweden the Python community is very big and active, which makes this conference very interesting.

A lot of nice talks today, a lot of them centered in data science and related topics, which was awesome,
as it is a very interesting field, and close to bioinformatics in some sense, which is what I work with.

I’ve tried to take some notes on the talks I have attended, and here are my thoughts/summary about them, with some links of interest.

# 1. Keynote – <u>Ian Ozvald</u>

Read more about Ian [here][ian].

Ian’s talk has focused on data science in general. One of the points that he has emphasized a lot,
is on the value of the data that a company owns _per se_. Doesn’t matter that your competitors know what machine
learning techniques or what algorithms do you use, because what matters is what _your data_ tells about _your customers_.
Your competitors are not gonna be able to replicate your results. The idea to keep in mind is then:
Data == Business value. Said that, he also said that even though "data mining", "data science" and
so on seems to be a trend, companies need to be careful, because you may just not need that.

Ian has gone through lots of examples of Python projects to help with data science,
i.e **[scikit-learn][scikit]**, [textract][textract], among others.

When talking about projects he developed, I found very interesting one in where he was using Optical
Character Recognition (OCR) to develop an app that would take pictures of the latin name
of the plants in the London botanic garden and link it to its content in Wikipedia.
If you think about that, this is pretty cool, you basically don’t need a database with plants information, because you already have it!

One last remark of the talk has been a guide for your first data science project,

* Iterate on
    * Visualize your data
    * Create milestones
    * [K.I.S.S][kiss]!
    * Think + hypothesize + test
    * **Communicate results**
        * ipython notebook

# 2. Analyzing data with Pandas – <u>Robin Lindeborg</u>

Robin’s GitHub [here][robin].

Robin has gone through a very nice introduction to Pandas, so if that is what you are looking for, you should definitely check his slides, that are available on his GitHub.

The topics covered have been very wide, including: data filtering, arithmetics on data frames and series, how to deal with missing values, etc. Lots of code examples, **I highly recommend** going through his slides.

At the end of the talk, he has conducted a life demo using data that corresponds to the military expenses from both USA and Sweden, from 1988 to 2015. I’ll let you guess who has been spending more money on armament ;-). Nice demo, nothing failing, which is quite surprising!

# 3. Docker and Python at Spotify – <u>Belhorama Bendebiche</u>

Belhorma GitHub [here][belhorama].

The talk started with a description of what Spotify was using before using Docker. Basically, he was mentioning things like Debian packaging, heavy puppet configurations and [clusterSSH][clusterssh], used for deployment with all the risks it implies (it basically replicated the same command across multiple hosts using ssh. These solutions had a lot of problems: Configuration mismatches, rolling back was hard, network issues, human errors, etc.

Now, they use intensively Docker. Docker basically creates a small linux container that its easily configurable. A linux container could be defined very _roughly_ as a process that "thinks" that is an isolated OS, having its own file system and everything it needs. A Docker build is configured using a dockerfile, that has commands to build the image, like dependencies and requirements. Each command is a layer and images can have parents.

The presentation finished with a nice demo of how a docker file and docker image looks like and how is it run. Unfortunately I can’t find his slides. Maybe some kind reader has? Please leave a comment!

# 4. Deep learning and deep data science – <u>Roelof Pieters</u>

Roelof GitHub [here][roelof].

Very genuine presentation, where Roleof has started asking us if we were a "cat person" or a "dog person". The talk has been driven by this question, describing how he build a classifier for taking pictures of cats and dogs to distinguish them.

Some of the tools or packages that he mentioned or used are scikit-learn, [caffe][caffe], [theano][theano] and ipython notebook. Caffe seems to be a very nice deep learning library, where you can find **pre-trained** models already available.

One message to take home is: The more features you have to classify your data, the better…**but** you have to be careful as well: more classifiers implies an exponential growth of the data.

The talk finished with some examples of deep learning used for audio and image recognition and some face recognition techniques, based on how the brain actually works.

He will publish the slides soon, I hope that in GitHub, otherwise I’ll update this blog post if I get to know where they’re published.

# 5. Hacking Human Language – <u>Hendrik Heurer</u>

Slides here, very nice ones!

This has been one of my favourites :). Hendrik is doing his Msc.Thesis in Natural Language Processing (NLP) at KTH in Sweden, and during the talk, he has gone through some of his projects or studies he has been carrying out.

To start with, he showed what seemed to be a map of Europe, and turned out to be a 2D plot of the GPS tag of thousands of flickr photo. Pretty neat :-). He continued with lots of examples of how you can use Python for NLP, like article content analysis or sentiment analysis, where he showed some examples (check the slides).

A **good source to start** learning, the **free** ebook [Natural Language Processing with Python][nlp].

Some other topics he covered are: Work tokenization, stemming (finding the root of a word), Part-of-speach tagging (is the work a noun? a verb?…) or named entity recognition (the word is a name, a place, a date, etc).

Very interesting how he described the process of converting words into vectors on an n-dimensional space, so that then you can do linear algebra on those vectors to get what you want. For example comparing the vectorial space of two different languages, you can translate from one to another only by looking at the position of a word in the original language space and looking at the same position in the space of the other language. (that may be a bit confusing…)

Ends up graphing his google searches and with a funny joke: The words "KTH" and "lazy" get really close in the space.

6. Python: How a Notebook is Changing Science – <u>Juan Luis Cano</u>

Juan Luis blog [here][juan_blog] (only Spanish). GitHub [here][juan_gh].

Nice talk describing how useful iPython Notebook is being in science. He uses [Russell's paradox][russell] to highlight the need of demonstrating both results, and procedure to get to those results.

IPython notebook is proven to be a very effective tool for that, giving the possibility of join code and rich explanations in a single place.

Several use case examples were shown in the presentation, all of them illustrating different aspects of iPython Notebooks, that from now one will be named [Jupyter][jupyter], which is a name made from **Ju**lia + **Py**thon + **R**, which are the platforms/languages that build the project. The big new thing about Jupyter is that it pretends to be language agnostic, allowing you to run even something called iMatlab (?!).

# Conclusions after the first day

Very nice presentations all of them. I am very pleased of having attended and I am looking forward for tomorrow! A bit nervous for the talk I am giving, but really willing to do it!

[ian]: http://ianozsvald.com/
[scikit]: http://scikit-learn.org/stable/
[textract]: http://textract.readthedocs.org/en/latest/
[kiss]: http://en.wikipedia.org/wiki/KISS_principle
[robin]: https://github.com/vienno
[belhorama]: https://github.com/mninja
[clusterssh]: http://sourceforge.net/projects/clusterssh/
[roelof]: https://github.com/graphific
[caffe]: http://caffe.berkeleyvision.org/
[theano]: http://www.deeplearning.net/software/theano/
[hendrik]: https://dl.dropboxusercontent.com/u/5041011/Heuer_Hacking_Human_Language_PyCon.pdf
[nlp]: http://www.nltk.org/book_1ed/
[juan_blog]: http://pybonacci.org/
[juan_gh]: https://github.com/Juanlu001
[russell]: http://rationalwiki.org/wiki/Russell%27s_Teapot
[jupyter]: https://jupyter.org/
