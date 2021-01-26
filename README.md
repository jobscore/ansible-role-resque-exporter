[![Build Status](https://travis-ci.org/jobscore/ansible-role-resque-exporter.svg?branch=master)](https://travis-ci.org/github/jobscore/ansible-role-resque-exporter)

Prometheus Resque Exporter role
=========

An Ansible role for installing Prometheus Resque Exporter on a Ubuntu box.
This role is based on https://github.com/jobscore/resque-exporter

Requirements
------------

Resque must be already installed.

Role Variables
--------------

```
resque_exporter_redis_url: Redis server url. Default to redis://localhost:6379
resque_exporter_redis_namespace: Redis namespace for resque. Default to resque
resque_exporter_port: The port in which the exporter will expose the metrics. Default to 9447
```

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
        - role: jobscore.prometheus_resque_exporter
          resque_exporter_redis_url: redis://redis-server:6379
          resque_exporter_redis_namespace: resque
          resque_exporter_port: 9447

License
-------

[MIT](/LICENSE)

Author Information
------------------

This role was created by [GlauberrBatista](https://github.com/GlauberrBatista) while working for [JobScore Inc](https://jobscore.com).
