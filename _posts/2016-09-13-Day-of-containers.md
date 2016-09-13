---
layout: post
title:  "Day of Containers - Docker Everything!"
date:   2016-09-13
comments: true
tags:
    - Docker
    - programming
    - CI
    - CD
    - devops
---

![Conference](/images/docker-day/conference.jpg)

Two weeks ago I attended the ["Day of containers"](http://www.code-conf.com/doc-sthlm-2016/) conference. Vacations and work got in the middle so I couldn't write this post before, but here it is! The reason I wanted to go to this conference and not others about docker is that this one was quite more like a workshop.

I've read about docker and its many pros and cons, but never put my hands on it, so I though it would be good to dedicate an entire day to it with real examples and experienced people in the field.

## Morning session

### _Self healing systems_
The conference started with the keynote speaker [Viktor Farcic](https://github.com/vfarcic) talking about _Self Healing Systems_.

Viktor began describing a "simple" architecture consisting on a couple of servers serving a couple of applications. One should start thinking about provisioning the servers in case you want to scale, write tests, build, deploy, test, build again, test again, etc.

To manage all of that, you should monitor, react to problems, **prevent** problems... don't you want as much automated as
you possibility can? During the talk, Viktor enters in a lot of detail about levels of self-healing systems (i.e application level,
system level or hardware level) and type of self-healing systems (i.e reactive healing and preventing healing). The important part of
the talk was imho when he talked about the requirements for these kind of systems. If I had to summarize, I would say:

* Ability to deploy to any server inside a cluster that meets hardware requirements
* Ability to deploy without downtime and to automatically scale and down-scale instances

To meet those two requirements, a Docker-based architecture is perfect since deployment becomes (almost) trivial due to
lack of dependency problems or installation problems. Same for scaling up and down without downtime.

### _Docker 101_
In Docker 101, [Andrey Devyatkin](https://twitter.com/andrey9kin) form Praqma guided us, the noobs in the Docker world,
through the basics of Docker. This was one of the workshops I was waiting for, I think is always better a 1h
hands on than a 1h talk.

During the workshop Andrey walked us through how to build a basic Docker image and how to run/kill/monitor containers and
modify images. It was very instructive and I don't really think its worth reproducing commands in here, there are
lots of how-to over the internet, just pick one :). I imagine [this one](https://www.youtube.com/watch?v=YgFPr2F8Ong&list=PLuvRKxeqrv4I9wxOs4_BDf3ltUCV02-sj&index=2) from Mike Long should
be about the same.

## Evening session

### _Building and observing services on Docker Swarm clusters. The latest and greatest from Docker, inspired by Netflix_

[Gergo Horanyi](https://github.com/ghoranyi) from Founders leaded a nice workshop in which we built a mini
Docker swarm network on two provided AWS instances. Fortunately he provided [a gist](https://gist.github.com/guillermo-carrasco/48d677cb4d384914f6094f89e80c23a7) with all the commands to
write so we could listen to the explanations at the same time that we _did_ the workshop.

No much to say about the workshop since it was 100% hands on. Instructive but to be honest I would have
appreciated a deeper explanation in how the communication layer works, which is still a mystery to me.

The coolest part of this talk/workshop was the deployment and demonstration of Netflix's Orchestration
tool called [Vizceral](https://github.com/Netflix/vizceral) **check that out!**.


### _Building hybrid microservices with Docker. [Michael Hausenblas](https://twitter.com/mhausenblas), Mesosphere_

Slightly disappointed with this talk. Not because of the content, which was great, but because it was very
much like the one given on the Keynote. Michael talked about the basics of Docker, **why** you should
use Docker and specially some good practices like release cycle and never to store credentials in
your images. Showed [example](https://github.com/mesosphere/training/tree/master/velocity-training-06-2016/ci-cd) of CI/CD.


### _Containers and the death of the Linux distribution_

[Kelsey Hightower](https://twitter.com/kelseyhightower) from Google gave a very engaging talk about how
several people thinks about the future of the linux _distribution_. Distribution != linux, just to be clear.

He reasons that its impossible to make a piece of software work on several linux distributions without having
to recompile to each one of them. Actually if you've ever worked as System Administrator you know what
I am talking about. You compile on Ubuntu and works, then compile in RedHat and you're missing a library, or
you have an old version of libc. Updating libc is a mess so you have a big problem.

Docker will solve/is solving all of those problems. Kelsey also talks about how some languages like Go are
trying to solve these problems as well with almost 0 dependency compiled applications. Go even implements
its own version of libc so that your application doesn't depend on the system's. Pretty neat talk in
general.

An example of the future is phone applications: Do you ever have to type Next, next, install dependencies
or have problems installing an app on your phone? Nope.

> The death of the linux distro is the first step towards decoupling applications from the machine

## Personal experience, conclusion

Ironies of life, when I was writing this blog post I realized that my ruby installation was broken since
my last OS update... yay!

```
(python3) ~/repos_and_code/guillermo-carrasco.github.com (master) ~> jekyll serve --drafts --config _config.yml,_config_devel.yml
WARN: Unresolved specs during Gem::Specification.reset:
      jekyll-watch (~> 1.1)
WARN: Clearing out unresolved specs.
Please report a bug if this causes problems.
/usr/local/lib/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/spec_set.rb:95:in `block in materialize': Could not find tzinfo-1.2.2 in any of the sources (Bundler::GemNotFound)
	from /usr/local/lib/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/spec_set.rb:88:in `map!'
	from /usr/local/lib/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/spec_set.rb:88:in `materialize'
	from /usr/local/lib/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/definition.rb:140:in `specs'
	from /usr/local/lib/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/definition.rb:185:in `specs_for'
	from /usr/local/lib/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/definition.rb:174:in `requested_specs'
	from /usr/local/lib/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/environment.rb:19:in `requested_specs'
	from /usr/local/lib/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/runtime.rb:14:in `setup'
	from /usr/local/lib/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler.rb:95:in `setup'
	from /usr/local/lib/ruby/gems/2.3.0/gems/jekyll-3.2.1/lib/jekyll/plugin_manager.rb:36:in `require_from_bundler'
	from /usr/local/lib/ruby/gems/2.3.0/gems/jekyll-3.2.1/exe/jekyll:9:in `<top (required)>'
	from /usr/local/bin/jekyll:22:in `load'
	from /usr/local/bin/jekyll:22:in `<main>'
```

Yeah looks like a problem with `tzinfo-1.2.2`, tried to fix that and got a problem with `json-1.8.0` or similar. And so on...
I spend a whole morning trying to fix this stupid errors and couldn't manage, and I don't want to! haven't I been
on a docker conference? Why not just run Jekyll on Docker? Fortunately for me, Jekyll people have
already thought about this and you have available a couple of [Jekyll Docker Images](https://github.com/jekyll/docker) to use.

So basically after pulling the image, I can run:

```
docker run --rm --label=pages --volume=$(pwd):/srv/jekyll -it -p 0.0.0.0:4000:4000 jekyll/jekyll:pages bundle exec jekyll serve --drafts --config _config.yml,_config_devel.yml
```

And I have my blog back and running. A bit of a long command, but you can always create an alias, and
I think I'll get better in the future.

Will I use Docker in my company? Probably not in the near future. I do see the unarguable value of Docker
and I think its the future, but I also think you shouldn't rush to it if you don't really need it. It
is a **very** fast changing and complicated architecture that will require a lot of effort. Maybe not the
best to start a project or POC. Read [this key article](https://circleci.com/blog/its-the-future/) from CircleCI blog to understand what I mean :smile:.

Please share if you enjoyed!
