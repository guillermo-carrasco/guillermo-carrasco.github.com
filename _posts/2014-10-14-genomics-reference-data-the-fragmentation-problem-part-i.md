---
layout: post
title:  "Genomics reference data: The fragmentation problem (part I)"
date:   2014-10-14
comments: true
tags:
    - openscience
    - genomics
---
If you work with genomics data, you know what I’m talking about. In order to perform
any kind of bioinformatics analysis, you need to have at least some of the following reference data:

* Reference genome for alignment, as well as index files for the alignment tool you’ll be using; i.e BWA, Bowtie, Bowtie2, etc.
* Variant Calling data (VCF files)
* Gene Transfer Data (GTF files)
* Annotation data (snpEff, VEP, Annovar)
* Genetic Variation data (dbSNP, etc)

<!--more-->

Maybe even more, depending on the type of analysis you’re doing. The fact is that
most of these data is dispersed around several servers and institutions. Not only that,
this data is stored without any particular standard on the different sources you can find it.
For example, if you want a particular piece of reference data for a particular organism,
you may have to follow a different tree structure and naming conventions that if you
want a different piece of reference data for the same organism if that last piece of data is stored on another server.

There are solutions that try to solve this problem making it transparent to the user
which is the source of the reference data (i.e [Cloudbiolinux][Cloudbiolinux] or [COSMID][cosmid]). However,
due to the aforementioned lack of standards on the storage and maintenance of these
data, these tools cannot always help.

Last July I was in Boston to attend the [BOSC conference][bosc] and previous hackathon.
And I thought it would be a good opportunity to ask around what people was doing
to solve this problem in their research groups. I set up a survey that participants
would fill in. I also tweeted the survey so that other people could fill it.

In the following lines, I’ll try to summarise and make some sense from the responses
I obtained. While I was writing, I realised that I have a lot to say, so I decided
to write it in (two?) parts. This is part I, Part II will come soon :-)

## Participation
I got a total of 42 responses from different organisations, including Harvard
Medicsurvey_participational School, Princeton University or MIT among other research groups.
The survey was open for one week (2014-07-07 to 2014-07-12), and I got most of the participation the first day.

<img src="/images/genomics_reference/survey_participation.png" alt="Survey participation" align="right">

A fair amount of research groups, I think. I want to thank everyone that participated in the survey.

## The questions
I must say that the format of the survey made it a bit complicated to parse the
results and extract information, I guess that’s something that one learns with experience as well.
My intention with the questions in the survey were to determine:

1. Are we doing something really wrong, or is it really a fragmentation problem with the reference data?
2. What is other people doing? What solutions are they implementing?
3. If the problem is real… what can we do?

<u>Question 1</u>: Do you work only with one species, or several species’ genomes?_

<img src="/images/genomics_reference/single_or_multiple_species1.png" alt="Single or multiple species" align="right">

I considered this question important because It is not the same if you have to sync
data from only one specie than if you have to get data from several species.
Even if different data for the same specie is located in different places, to automate
it is not difficult if you don’t have to plug in and/or update new species’ data continuously.
It turns out that most of the groups are working with several species.

This is our case as well, and actually I find this group more interesting for the purpose of this survey, so great that is the clear majority of the cases.

<u>Question 2</u>: What kind of reference data do you use for your research?_

![Reference Usage](/images/genomics_reference/reference_usage.png)

From above’s plot one can see that there is a subset of reference data which use is
common for almost everyone: Reference Genome and Index Files, with Reference Genome
being used by everyone that answered the survey (well, except one…). This is expected
given the fact that this data is used in the alignment step, the most common in a typical
genomics analysis. Other common data among groups is GTF, VCF, GVF and annotation data.

Other custom-ish data like [BED-detail][bed_detail] or hand-made annotation tab-delim files…
are as expected less common.

Here in the National Genomics Infrastructure in Sweden we use Reference Genome,
Index files for several aligners and all the data in the more common groups.

<u>Question 3</u>: Where do you fetch your data from?_

![Reference locations](/images/genomics_reference/reference_data_locations2.png)

This is the question I was more interested in, because what made me think on this survey was the fact that:

1. We always need to download new data and update existing one
2. We do it in a semi-automated way because we don’t know any better…

The first thing I noticed is that the three most used places for downloading data are [UCSC][ucsc],
[ENSEMBL][ensembl] and [BioMart][biomart]. I think that everyone knows both ENSEMBL and UCSC,
where you can download lots of reference data, but what I was not aware of was about BioMart
(shame on me?). BioMart seems to be an effort to federate scientific data. What they say is:

1. Set up your own data source with a click of a button
2. Expose your data to a world wide scientific community through BioMart Portal.
3. Federate your local data with data from other community members

Basically, one can set up a node for sharing data, this node or database can then be listed in BioMart,
together with the datasets that it contains, and you can then download that dataset  
later (applying some filters if you want to). The idea is good, but still we have the
initial problem: What do you do if you can’t find a dataset that contains all the data you need?
You look for it in another dataset and keep going… Also, it is very dependent on their software.
I would like to see more common protocols being used.

In this survey, up to 17 reference data sources were listed… it is clear that there is a need for unification.

## Conclusions (part I)
First of all, please feel free to explore the data yourself, you can find the parsed
responses (without personal data) [here][responses], together with the Ipython notebook I’m using
to analyze the data.

With this first part of the survey’s responses I could see basically that we are a
common use case: We use data from several species, download lots of different data and
from different places. Also, I discovered new reference data sources, like BioMark,
a very good initiative, imho.

There are lots of places where to download the data you need, and if you start reading about them,
it is quite frustrating to see how they diverge. Something that should be simple because
is the base for any analysis, can become very time consuming.

On the second part(s) of the survey, I’ll go through the questions:

* How do you fetch the reference data?
* What tools do you use for fetching reference data?
* How do you keep your reference data up to date?
* How do you structure the reference data?
* Where do you store your reference data?
* Comments

Seems like I still have some homework to do.

I would love to start a discussion about this, so feel free to put your comments below. As I said, part II will come soon.

Hope you found this interesting!


[Cloudbiolinux]: https://github.com/chapmanb/cloudbiolinux
[cosmid]: https://github.com/robinandeer/cosmid
[bosc]: http://www.open-bio.org/wiki/BOSC_2014
[bed_detail]: http://genome.ucsc.edu/FAQ/FAQformat.html#format1.7
[ucsc]: https://genome.ucsc.edu/
[ensembl]: http://www.ensembl.org/index.html
[biomart]: http://biomart.org/
[responses]: https://github.com/guillermo-carrasco/guillermo-carrasco.github.com/tree/master/codes/genomics_reference
