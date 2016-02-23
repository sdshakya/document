#!/usr/bin/env python
import os
import getpass
import time
import sys


def db_restore():
    print "Enter user:"
    user = raw_input()

    print "Password will not be visible:"
    password = getpass.getpass()

    print "Enter host:"
    host = raw_input()

    print "Enter database name:"
    database = raw_input()
    
    print "Enter Database file name to be restored:"
    dbfilename = raw_input()
    
    os.popen("mysql -u%s -p%s -h%s %s < %s.sql" % (user,password,host,database,dbfilename))
    print ("mysql -u%s -p%s -h%s %s < %s.sql" % (user,password,host,database,dbfilename))
        	
db_restore()


