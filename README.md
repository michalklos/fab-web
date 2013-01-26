Author:michalklos

Fab-Web
=========

web.py wrapper for fabfile files.

It's for if you want to call your fab functions as a web service.

Works with GET requests, passing params in query string.
    Fabric env is set by keys that match keys in env (e.g. ?host_string=foo)
Works with POST requests, passing params as json data.
    Fabric env is set by env dictionary in json (e.g. {"env":{"host_string":"foo"}}

Pre-requisites
==============
web.py
   http://webpy.org/install

fabric
   http://docs.fabfile.org/en/1.5/

To run locally
========
drop fabweb.py in directory with your fabfile then...
python fabweb.py

Example usage
=========
GET:
curl 'http://0.0.0.0:8080/run_command?cmd=uname'

GET with Fab env:
curl 'http://0.0.0.0:8080/run_remote_command?cmd=uname&host_string=localhost&user=mklos'

POST:
curl --data '{"cmd":"uname","env":{"host_string":"localhost","user":"mklos"}}' http://0.0.0.0:8080/run_remote_command

