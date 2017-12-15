#!/usr/bin/python
#use python 2.7

import commands
import sys 

if sys.argv[1] == "start":
    print 'start...'
    (status, output) = commands.getstatusoutput('/usr/local/nginx/sbin/nginx')
    if status != 0 :
	print output
	sys.exit()
    (status, output) = commands.getstatusoutput('/usr/local/php7/sbin/php-fpm')
    if status != 0 :
    	print output
	sys.exit()
    print 'successfully!'

if sys.argv[1] == "restart":
    print 'restart ...'
    (status, output) = commands.getstatusoutput('/usr/local/nginx/sbin/nginx -s reload')
    if status != 0:
	print output
	sys.exit()
    (status, output) = commands.getstatusoutput('cat /usr/local/php7/var/run/php-fpm.pid')
    if status != 0:
    	print output
	sys.exit()
    (status, output) = commands.getstatusoutput('kill -USR2 ' + output)
    if status != 0:
	print output
	sys.exit()
    print 'successfully!'
