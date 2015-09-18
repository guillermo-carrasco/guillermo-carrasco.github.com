---
layout: post
title:  "Parsing and building XML files with python"
date:   2013-07-26
comments: true
tags:
    - programming
    - Python
    - XML
    - parsing
---
[JSON][json] is nowadays the most common way of “talking” with APIs and saving configuration files.
However, there is still a lot of software and APIs that use XML format. Actually,
our new [LIMS][LIMS] uses XML to present API queries results, as well as some of the software
that we use to analyze and manipulate sequencing data.

When I had to deal with XML for the first time with Python I had a lot of troubles
parsing and building files. The documentation is not clear at all, and there seems
to be tens of ways for doing the same thing… I will limit myself to explain the **basic**
[xml.etree.ElementTree][ElementTree] concepts and file operations so you can understand
and work with basic XML files in Python.

# ElementTree and Element
First, lets define our XML file. Suppose we want to store an XML file that describes
programming languages and some information about them. We start with this simple test.xml:

{% highlight xml %}
<Languages>
    <Python version="2.7">
        <Properties interpreted="yes" />
    </Python>
</Languages>
{% endhighlight %}

This file is simple but at the same time has all what we need. The first thing to do is parse the file:

{% highlight python %}
from xml.etree import ElementTree as ET

lang = ET.parse('test.xml')
{% endhighlight %}

If we check the type of the variable lang, we’ll see that this is ElementTree.
**An ElementTree represents the whole XML file**. ElementTree has some searching
functions to find specific children, for example _lang.find(‘Python’)_ will return the first child.

A [well-structured XML][good_xml] file should have one (and only one) root.
The root, as well as all its elements (called children), are of the type Element.
Elements are blocks of XML and can be nested. They have two basic properties:
the **tag** and the **attributes**.
The tag is the “name” of the block, and attributes is the list of attributes of the block. Let’s see this in our example:

{% highlight python %}
In [10]: languages = lang.getroot()
In [11]: type(languages)
Out[11]: xml.etree.ElementTree.Element
In [12]: list_languages = languages.getchildren()
In [13]: type(list_languages)
Out[13]: list
In [14]: list_languages
Out[14]: [<Element 'Python' at 0x101069c10>]
In [20]: python = list_languages[0]
In [21]: python.tag
Out[21]: 'Python'
In [22]: python.attrib
Out[22]: {'version': '2.7'}
{% endhighlight %}

As you can see, children of XML Elements are list of Elements. As they’re lists,
you can apply list operations such as _append_ or _extend_. In fact, this is how you modify the document.
The same happens with the attributes of that Elements, which are dictionaries,
and therefore you can apply any dictionary-like operation to them.

# Modifying the XML file
How to modify the XML file? Imagine we want to modify the Python description.
For example, we could want to add a new property that describes how the typing is done.
As said before, attributes are dictionaries, so we just need to add the corresponding (key, value) pair:

{% highlight python %}
In [23]: python_properties = python.find('Properties')
In [24]: python_properties.attrib['typing'] = 'duck'
{% endhighlight %}

What if we want to add another child, for example one that lists some language-related
projects? Well, is just a matter of creating a new Element and appending it to the Python Element:

{% highlight python %}
In [25]: projects = ET.Element('Projects')
In [26]: django = ET.Element('Django', type='Web Framework')
In [27]: projects.append(django)
In [28]: #And so on...
In [29]: python.append(projects)
{% endhighlight %}

At this moment, our XML looks like this:

{% highlight xml linenos %}
<Languages>
    <Python typing="duck" version="2.7">
        <Properties cross-platform="yes" typing="duck" />
        <Projects>
            <Django type="Web Framework" />
        </Projects>
    </Python>
</Languages>
{% endhighlight %}

Easy peasy, rigth? What about adding a new programming language to the list?

{% highlight python %}
In [30]: c = ET.Element('C')
In [31]: c.attrib['cross-platform'] = 'yes'
In [32]: c.attrib['typing'] = 'static'
In [33]: languages.append(c)
In [34]: #And yes, you can add more properties, projects, etc...
{% endhighlight %}

And here we have our final XML:

{% highlight xml linenos %}
<Languages>
    <Python typing="duck" version="2.7">
        <Properties cross-platform="yes" typing="duck" />
        <Projects>
            <Django type="Web Framework" />
        </Projects>
    </Python>
    <C cross-platform="yes" typing="static" />
</Languages>
{% endhighlight %}

Writing back the XML to a file is as easy as calling the method _write_ of the ElementTree
that represents the document (_lang_ in our case).

And thats it! I hope that this post helps a little bit in the tedious task of
working with XML files in python. If so, share! :-)



[json]: http://en.wikipedia.org/wiki/JSON
[LIMS]: http://en.wikipedia.org/wiki/Laboratory_information_management_system
[ElementTree]: http://docs.python.org/2/library/xml.etree.elementtree.html
[good_xml]: http://en.wikipedia.org/wiki/XML#Well-formedness_and_error-handling
