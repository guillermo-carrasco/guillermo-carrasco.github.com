---
layout: post
title:  "Setting up a testing SLURM cluster"
date:   2013-07-17
comments: true
tags:
    - automation
    - programming
    - devops
    - SLURM
    - VAGRANT
---
So I’m in Berlin these days participating in [Codefest][codefest2013] 2013 with a lot of awesome
developers from all around the world. As a first task, me and two other colleges
are implementing a SLURM connector for IPython Parallel.

SLURM is the batch scheduler that is used in UPPMAX HPC, where we execute our analysis.
In order to test our connector, we could run our tests on UPPMAX, but this implies putting
our tests in the queue, which usually takes time… we’re in a two days hackathon,
so we’ve to speed up things as much as we can!

<!--more-->

Taking advantage of the situation I would like to explain how to create a mini-local
cluster in order to test things things that require a cluster. To set up a local testing
cluster, the only thing you need is Vagrant installed in your machine. I’ve tested
SLURM with Ubuntu 12.04 LTS box, you can easily add this box to your system running:

`vagrant box add precise64 http://files.vagrantup.com/precise64.box`

Once you’ve added Ubuntu box to your system, is time to spawn a multi-VM environment
and set it up. To do so, you just need to follow these steps:

1. Create the virtual machines: You can use this Vagrantfile from my GitHub to do so.
It will create two VM visible between them (a controller and a server/worker),
and will install SLURM in both of them. It will also copy a very basic SLURM configuration
file that can be also found in my GitHub account. Run the following command in the
same directory where you have downloaded the Vagrantfile:

    `vagrant up`

2. Unfortunately we have to do some manual steps now. SLURM uses [MUNGE][munge]
for authentication, and we  have to set it up. Both machines need to have the same
MUNGE security key. Connect to the controller (will also work if you connect to the server),
and create a MUNGE security key:

    `sudo /usr/sbin/create-munge-key`

3. Then, copy the key to the other machine. If you created the key in the controller:

    `sudo scp /etc/munge/munge.key vagrant@server:/home/vagrant/`

4. In the server, copy the key from the vagrant home to the corresponding configuration
directory and change the ownership to munge user:

    ```bash
    sudo cp ~/munge.key /etc/munge
    sudo chown munge /etc/munge/munge.key
    ```

5. Start MUNGE daemons in both machines:

    `sudo /etc/init.d/munge start`

6. Finally, run SLURM services:
    * On the controller: `sudo slurmctld -D &`
    * On the server: `sudo /etc/init.d/slurm-llnl start`

And that’s all! You can now submit jobs to your mini SLURM cluster, try it out with
this simple batch script:

```bash
#SBATCH -p debug
#SBATCH -n 1
#SBATCH -t 12:00:00
#SBATCH -J some_job_name


ls / > /home/vagrant/slurm.out
```

Run it using:

`sbatch test.sh`

You can use the same VM configuration to test other things that require a cluster (Hadoop?).

NOTE: A hackathon is a hackathon, you need to set up things quickly to test your stuff,
but please have in mind that bad practices for sites in production have been carried out in this post:

* Hard-coded IPs, scripts and URLs: BAD! Always use configuration files for these purposes.
* Software provisioning through shell commands like apt-get install: BAD! Use software provisioners: Chef, Puppet, etc.

BTW, check out [Valentine Svensson][vale] and [Roman Valls][roman]‘ blogs, those are the colleges
I’m working with right now :-)

<!--Links-->
[codefest2013]: http://www.open-bio.org/wiki/Codefest_2013
[munge]: https://code.google.com/p/munge/
[vale]: http://nxn.se/
[roman]: http://blogs.nopcode.org/brainstorm/
