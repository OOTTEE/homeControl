#!/usr/bin/python
from flup.server.fcgi import WSGIServer
from homeControl import app

if __name__ == '__main__':
	WSGIServer(app, bindAddress='/var/www/homeControl/fcgi.sock').run()
