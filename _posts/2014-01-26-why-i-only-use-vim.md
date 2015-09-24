---
layout: post
title:  "Why I only use VIM"
date:   2014-01-26
comments: true
tags:
    - editors
    - vim
    - programming
---
This is not a technical blogpost, I only want to share my feelings and experiences
with my favourite programming editor. I have been developing software for 7 years now –
including my years in the university – and in all these years I’ve tried **a lot** of editors.

It has been a while though since I only use VIM for development. And here are my top 5 "why" reasons:

<!--more-->

1. **Multiplatform**: As I said, I’ve tried a lot of editors during this years,
and one of the reasons for that is the platform dependence of some of them.
Depending on the project or job, I work on different platforms. Even if it does
not seem to be important, getting used to the tools you use increases your productivity.
You’ve to reach that point in where you stop thinking how to do something, and you just do it.
Changing your programming editor because you’re working on a different platform doesn’t help.

2. **Versatile**: VIM has everything that you’d want from a text editor, it’s just that
is not as easy to find, I give you that. You can open several files on different windows,
split windows and move around them, search regular expressions in your files, etc. Just _all_ you need:

    ![vim]({{ site.url }}/assets/images/why_i_only_use_vim/vim.png)

3. **Light**: I don’t say that there aren’t other good IDEs over there that does all of this and they’re multiplatform, but man, I just don’t want to have half of my RAM occupied by an opened editor, or see how my computer slows down when I open it, I just don’t want to. VIM is one of the lightest editors I’ve worked with ever.

4. **Easily configurable**: One of the things I love about VIM is the easiness of configuration.
Grab a coffee, read the [configuration options](http://vimdoc.sourceforge.net/htmldoc/options.html)
and start writing your own .vimrc file. Or, as I did, start working from an already existing
.vimrc file and just add or remove presets as you need. You can take a look at mine [here](https://github.com/guillermo-carrasco/dotfiles/blob/master/.vimrc).
I recommend you to put this file on a public site, and everywhere you go, you’ll
have your personalized editor just copying this file to your home directory.

5. **Plugins**: If you miss something, there are hundreds of plugins over there that
will make VIM ever greater. For those who miss autocompletion for example, there
is an awesome plugin called [YouCompleteMe](https://github.com/Valloric/YouCompleteMe)
that will allow you to do thinks like this:

    ![vim]({{ site.url }}/assets/images/why_i_only_use_vim/ycm.gif)

Finally, a plus reason: It’s everywhere out of the box! (well I’m thinking on serious systems,
of course you have to install it by yourself on Windows). This means that no matter
if you’re working on your computer or remotely on a server, you’ll have the same editor
wherever you work. Not having to change the editor for doing specific tasks is just a blessing, believe me.

And that’s all I wanted to say about VIM and why I use it. What do you guys think?
