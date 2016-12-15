---
layout: post
title:  "Understanding logging in Python"
description: The standard logging library seems to be a confusing part in the Python programming language. In my case...
date:   2016-12-15
comments: true
tags:
    - Python
    - Logging
    - metrics
    - devops
    - monitoring
---

The standard logging library seems to be a confusing part in the Python programming language. In my case, my
application was growing into several modules, sharing loggers, creating new ones, etc. I was getting weird behaviors like repeated log records or missing ones. I didn't really understand why until I dug into the (rather long) documentation.

This post pretends to be an overview on how Python logging works. For full details, you have
[plenty of documentation available][logging_docs].

## Main concepts

There are 4 main concepts in Python logging:

1. **Loggers** expose the interface that application code directly uses
2. **Handlers** send the log records (created by loggers) to the appropriate destination
3. **Filters** provide a finer grained facility for determining which log records to output
4. **Formatters** specify the layout of log records in the final output

You can add from zero to several `handlers` to the same `logger`. In the same way, you can apply from zero to
several `filters` to `handlers` _or_ `loggers`.

First important thing you need to know is that the logging module in Python is implemented as a hierarchy of
`loggers`, being the `RootLogger` the main one. Being so, any `logger` you create will be a descendent of
the `RootLogger`. Thus all the handlers and filters applied to the `RootLogger` will be applied to the
rest of the loggers. It is very important to have this in mind while configuring your logging strategy.
For example, you probably don't want to add a `FileHandler` to the `RootLogger`, since that will make
**all** the log records from your code _and_ the libraries you use to be stored in a file.

The second important concept is that you can create descendants of a logger this way:

```python
import logging

parent_log = logging.getLogger('parent')
child_1 = logging.getLogger('parent.child_1')
child_2 = logging.getLogger('parent.child_2')
```

`child_1` and `child_2` will now inherit handlers, formatters and filters from `parent_log` (as well
as from `RootLogger`).

## Log levels

As with any decent logging library, `loggers` can be configured in different levels. The level assigned
to a logger determines the log records it will process. A logger will only process logs with a level
equal or higher from which it was configured. Levels are `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`, in
that order. So a logger configured in level `WARNING` (the default with the `RootLogger`) will process
log records tagged `WARNING`, `ERROR` and `CRITICAL`. But not `DEBUG` or `INFO`.

## Example - Configuring logging

There are mainly two ways of configuring logging: via code or via configuration files. I personally
think its always better to separate the configuration from the code, so let's write a configuration
file. **We want to log everything on the console, but only those records from our app to a file for
longer term storage**. To do so, we will attach a [`StreamHandler`][StreamHandler] to the `RootLogger`. This will
"swallow" all the records and spit them in the console. To save the records from our app (called `myapp`)
we will attach a [`RotatingFileHandler`][RotatingFileHandler] to the main logger of our app. We only need to add it to the parent
logger, since all descendants will inherit it. Here is the configuration:

```yaml
version: 1

formatters:
    custom_format:
        format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

filters:
    myapp:
        name: myapp

handlers:
    console:
        class: logging.StreamHandler
        formatter: custom_format
    file:
        class: logging.handlers.RotatingFileHandler
        formatter: custom_format
        filename: myapp.log
        filters: [myapp]
        maxBytes: 1024
        backupCount: 5

loggers:
    '':
        handlers: [console]
        level: INFO
    myapp:
        handlers: [file]
        level: INFO
```

_NOTE: `''` its a special name to modify the `RootLogger`_

Hopefully the configuration file is quite self-explanatory once you know the parameters each handler
requires. Now you only need to load the configuration and start logging:

```python
import yaml
import logging
import logging.config

with open('config.yaml', 'r') as f:
    conf = yaml.load(f)

logging.config.dictConfig(conf)

myapp = logging.getLogger('myapp')
myapp.info('This logger will write both to console and to the logging file, since the logger\'s name is myapp')

myapp_api = logging.getLogger('myapp.api')
myapp_api.info('This should also write to both since its a descendant of myapp')

another_logger = logging.getLogger('another_app')
another_logger.info('This instead should only appear in the console')
```

If you run that code, this will be the output in the console:

```
2016-12-15 10:57:05,344 - myapp - INFO - This logger will write both to console and to the logging file, since the logger's name is myapp
2016-12-15 10:57:05,345 - myapp - INFO - This should also write to both since its a descendant of myapp
2016-12-15 10:57:05,345 - another_app - INFO - This instead should only appear in the console
```

And this will be the content of the file `myapp.log`:

```
2016-12-15 10:58:13,631 - myapp - INFO - This logger will write both to console and to the logging file, since the logger's name is myapp
2016-12-15 10:58:13,631 - myapp.api - INFO - This should also write to both since its a descendant of myapp
```

## Conclusions
Once you understand the main concepts, logging with the Python standard library it's actually quite pleasant
and flexible. It allows you to configure complex logging architectures and modify its behavior without
having to modify your application code.

Logging is very important for any application to gather analytics, detect anomalies and troubleshooting.
Hopefully this blog post has enlightened you a little bit and you're excited to try out a good logging
configuration :smile:.


<!-- Links -->

[logging_docs]: https://docs.python.org/3/library/logging.html
[StreamHandler]: https://docs.python.org/2.7/library/logging.handlers.html#logging.StreamHandler
[RotatingFileHandler]: https://docs.python.org/2.7/library/logging.handlers.html#logging.handlers.RotatingFileHandler
