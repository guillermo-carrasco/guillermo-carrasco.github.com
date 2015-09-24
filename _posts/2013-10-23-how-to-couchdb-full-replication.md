---
layout: post
title:  "How to: CouchDB full replication"
date:   2013-10-23
comments: true
tags:
    - automation
    - couchdb
    - databases
    - nosql
    - pytthon
    - replication
---
If you use CouchDB, for sure you know about the replication feature. It is quite
handy and easy to use, with a single POST request you can trigger the replication of an entire database.

The problem comes in the small (but important) details. When I first tried to
replicate all the databases from our CouchDB in production to our CouchDB for development,
I encountered three problems: The _users database, the design documents and the
security attributes of the databases were not being replicated.

The _users database and the design documents have the same solution: You just
need to be admin in order to replicate them. Citing the [CouchDB documentation][docs]:

> Only server and database admins can create design docs and access views.

What this means is that, in the POST request that you use to trigger the replication,
you have to prepend the admin credentials, something like:

```
curl -H 'Content-Type: application/json' -X POST http://localhost:5984/_replicate -d ' {"source": "http://admin:admin_password@production:5984/foo", "target": "http://admin:admin_password@stage:5984/foo", "create_target": true, "continuous": true} '
```
This POST request will also work with the _users database.

At this point you have your database with its views replicated but… everyone with
an account can do anything he wants on it! :-/. Ok let’s see, again reading the documentation,
we find the following information:

> Note that security objects are not regular versioned documents (that is, they are
not under MVCC rules). This is a design choice to speedup authorization checks
(avoids traversing a database’s documents B-Tree).

What this means is that, as security objects are not versioned, they cannot be replicated,
because replication in CouchDB is based on versions. The solution I found, and works
pretty well, is to explicitly copy this object. How? Well, this object is just another
JSON document, so you just need to GET it from the original database, and PUT it in the
destination one. Would be something like this:

```
curl -X GET http://admin:admin_password@localhost:5984/foo/_security | xargs curl -H 'Content-Type: application/json' -X PUT http://admin:admin_password@localhost:5984/foo/_security -d {}
```

Yay! This way you have the database foo completely replicated.

Last but not least, If you’ve read my other posts you may have noticed that I am
quite a fan of automation, and I usually program in Python. [Here][script] you have a little present. 
This script can be used to automatically set up continuous replication from a source database
to a destination database. It also has an option to trigger a cloning: The destination
database will be **completely removed** and the source database will be cloned there.
Be careful and use it at your own risk ;-).

An idea of how to use it: We have set a continuous replication from our production
database to our stage database. Once a week, **as agreed with all developers**,
we put back the stage database at the same state than the production one.

Hope this post helps! If it does, share!


[docs]: http://wiki.apache.org/couchdb/Replication
[script]: {{ site.url }}/assets/codes/couchdb_full_replication/couchdb_replication.py
