---
layout: post
title:  "The dangers of mutability in Python"
date:   2022-01-12
comments: true
tags:
    - python
    - memory management
    - coding
    - object oriented
---
<blockquote class="twitter-tweet" align="center" data-cards="hidden"><p lang="en" dir="ltr"><a href="https://twitter.com/hashtag/TIL?src=hash&amp;ref_src=twsrc%5Etfw">#TIL</a> that when using the * operator on lists in <a href="https://twitter.com/hashtag/Python?src=hash&amp;ref_src=twsrc%5Etfw">#Python</a>, it does _not_ create a copy of the elements in the list, but rather references to them 🤯. Be careful if you&#39;re creating a binary mask this way... <a href="https://twitter.com/hashtag/pythontricks?src=hash&amp;ref_src=twsrc%5Etfw">#pythontricks</a> <a href="https://t.co/LKYPudAmmy">pic.twitter.com/LKYPudAmmy</a></p>&mdash; Guillermo Carrasco (@guillemch) <a href="https://twitter.com/guillemch/status/1470434844236783618?ref_src=twsrc%5Etfw">December 13, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

> Disclaimer: This whole article's insights are based on the most common implementation of Python: [CPython][cpython].

A few weeks ago, I stumbled upon this weird behaviour: I was trying to solve one of the [Advent Of Code][aoc] problems using a 
binary matrix. I realised that, when updating a specific position in the matrix, I was updating other positions I did not 
intend to. The issue is very easy to reproduce, as you can see in the tweet above.

<!--more-->

I did not understand what was happening, and this led me into a deep rabbit whole of Python mutability, how specific operators 
work, and how Python manages memory and references to objects.

## The Object Realm

Before digging deeper into my specific issue, it's important to understand the common sentence "In Python, everything is 
an object". What do we mean with that? Other languages like C or Java have [primitive data types][primitive_types] such as **char**, **int**
or **float**. In those languages, the mentioned types hold the true value of the char, int or float they represent, in bytes. 
So when you declare a variable `int a = 2` in C, the variable `a` is actually holding the binary representation of the integer `2`. 
When you create a new variable with the same value, new space in memory is reserved to hold the same binary representation 
of the number `2`.


This is not the case in Python. When you declare an integer variable in Python, that variable has properties and methods you can access. For example:

```python
In [1]: x = 2337
In [2]: x.real
Out[2]: 2337
In [3]: x.bit_length()
Out[3]: 12
```

In fact, technically Python does not declare variables, but rather _names_ that point to objects. Those objects are called 
_PyObjects_, and they are the Python binding to the C representation of the data they are holding.

A PyObject is a structure that contains three information pieces:

* the data type is referencing -- _int_, _float_, ...
* the value
* a reference count

This illustration may help you visualise what a PyObject is:

![pyobject](/images/dangers_of_mutability/pyobject.png)
*Image extracted from [The Real Python's course][real_python] on Pointers and Objects in Python*

<br>

Generally when creating a new variable, a new PyObject is created and its reference count starts at 1. If more variables 
reference the same object, the reference count is incremented. When no variables reference that object anymore, the object 
is destroyed from memory. This process is automatic in Python and it's called _Garbage Collection_. A way of knowing the 
memory address of an object in Python is by using the built-in function `id()`:

```python
In [4]: print(hex(id(a)))
Out[4]: 0x10d0fb7d0

In [5]: b = a

In [6]: print(hex(id(b)))
Out[6]: 0x10d0fb7d0
```
_(memory addresses are generally represented in hexadecimal)_

As you can see, when creating a variable by using the assign operator `=`, you are just creating another reference to the 
same memory space (`0x10d0fb7d0` in this specific case, it will be different if you replicate this example).

When creating new variables/objects, new addresses are used:

```python
In [7]: c = 123

In [8]: print(hex(id(c)))
Out[8]: 0x10d0fc1f0
```

## Some special cases -- Interning

While this is not really relevant for our particular case, I learned something very interesting while reading about memory 
management in Python. Look carefully at these lines of code:

```python
In [9]: a = 42

In [10]: b = 42

In [11]: c = 12345678

In [12]: d = 12345678

In [13]: print(hex(id(a)))
Out[13]: 0x10d0fb7d0

In [14]: print(hex(id(b)))
Out[14]: 0x10d0fb7d0

In [15]: print(hex(id(c)))
Out[15]: 0x7f998807eb30

In [16]: print(hex(id(d)))
Out[16]: 0x7f998807ed10
```

If you didn't notice, the addresses of `c` and `d` are different, but the addresses of `a` and `b` are the same?! 
If every time we create a new variable, a new object is created... shouldn't all 4 addresses be the different?


It turns out that, in order to save memory and gain efficiency, Python pre-loads in memory some of the most commonly used values. 
Those are, apparently, integers in the range `[-5, 256]`, some strings, the `None` object, and more.

This process is called **interning**, and you can read more about it in [this][interning] blog post.

## Be careful with your mutable objects
We are getting close to being able to explain the behaviour of my binary mask. But before that, one more concept. 
If you've worked with Python or any other programming language long enough, you are probably familiar with the concept of 
mutability. Simply put, an object is **mutable** if you can change its value, and **immutable** if you can't.

Some examples of mutable objects in Python are lists, dictionaries or sets. Other objects like integers, strings or tuples
are immutable.

Have you ever seen something like this?

```python
In [17]: l1 = [1, 2, 3]

In [18]: l2 = l1

In [19]: l1
Out[19]: [1, 2, 3]

In [20]: l2
Out[20]: [1, 2, 3]

In [21]: l2.append(4)

In [22]: l1
Out[22]: [1, 2, 3, 4]
```

When creating `l2`, we are really only pointing to the same memory address as `l1`. Since a list is a mutable object, 
appending on `l2` is effectively the same as appending on `l1`, and thus we are unintentionally modifying `l1` too. 
If we would like to avoid this behaviour, we need to create two separate list objects, like this:

```python
In [23]: l1 = [1, 2, 3]

In [24]: l2 = [1, 2, 3]

In [25]: l1
Out[25]: [1, 2, 3]

In [26]: l2
Out[26]: [1, 2, 3]

In [27]: l2.append(4)

In [28]: l1
Out[28]: [1, 2, 3]

In [29]: l2
Out[29]: [1, 2, 3, 4]
```
(_you can as well use the `copy()` operator on `l1` to create an identical list_)

This is the expected behaviour. I've seen a lot of novice Python developers stumble upon this issue. 
[Default mutable arguments][default_arguments] are another common source of nail-biting and hair pulling.

## The `*` operator for lists in Python

And finally, we are able to explain the behaviour of the binary matrix. The reason why I entered this rabbit whole of 
memory management and mutability... 

It turns out that, contrary to what I thought, the repetition operator for lists (`*`) in Python does not create new objects, 
but rather creates _references_ to the original one. In my case, I wanted to create a 3x5x5 matrix, but let's simplify 
for the sake of an example, and say I want to create a 3x3 boolean matrix. I would do:

```python
In [30]: l1 = [[False, False, False]]*3

In [31]: l1
Out[32]: [[False, False, False], [False, False, False], [False, False, False]]
```

and then I want to modify just the first position of the first row:

````python
In [33]: l1[0][0] = True

In [34]: l1
Out[34]: [[True, False, False], [True, False, False], [True, False, False]]
````
(_note that the first position of *all* the rows has been modified_)

By now, you should quickly see what's happening: The `*` operator is not creating new lists, but rather referencing the 
same one three times. So when updating the first position of the first row, I am really updating all other rows, 
since they are the exact same object in memory.

How would you achieve the desired behaviour? Well, there are many ways. You could for example use the `copy()` method, 
which creates a true copy of the object rather than a reference:

```python
In [35]: row = [False, False, False]

In [36]: l1 = [row.copy(), row.copy(), row.copy()]

In [37]: l1
Out[37]: [[False, False, False], [False, False, False], [False, False, False]]

In [38]: l1[0][0] = True

In [39]: l1
Out[39]: [[True, False, False], [False, False, False], [False, False, False]]
```

or programmatically, use a list comprehension like this:


```python
In [40]: l1 = [[False, False, False] for _ in range(3)]

In [41]: l1
Out[41]: [[False, False, False], [False, False, False], [False, False, False]]

In [42]: l1[0][0] = True

In [43]: l1
Out[43]: [[True, False, False], [False, False, False], [False, False, False]]
```

However, this is rather cumbersome, and I would recommend going for [numpy arrays][numpy_arrays] instead.

## Conclusions
Python memory management, while in most cases is very convenient and eases our lives greatly, can sometimes be the 
source of confusion and weird behaviour. It is thus very important for us to understand how objects and variables are created, 
if the objects we are using are mutable or not, what and how are we passing as function arguments and so on.

I also really recommend that when you see some strange behaviour, something you don't understand, really try to get to the 
root of it. I learned a lot about Python memory management while investigating this issue, as I hope you did while reading 
this summary.

Have a nice one! And feel free to ask me any question in the comments :blush:

<!-- Links -->

[cpython]: https://en.wikipedia.org/wiki/CPython
[aoc]: https://adventofcode.com/2021/day/4
[primitive_types]: https://en.wikipedia.org/wiki/C_data_types
[real_python]: https://realpython.com/lessons/variables-c-vs-python/
[interning]: https://towardsdatascience.com/optimization-in-python-interning-805be5e9fd3e
[default_arguments]: https://florimond.dev/en/posts/2018/08/python-mutable-defaults-are-the-source-of-all-evil/
[numpy_arrays]: https://numpy.org/doc/stable/reference/generated/numpy.array.html
