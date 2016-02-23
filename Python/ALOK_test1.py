#! /usr/bin/python

import os
import time
import datetime
import getpass
import logging
import subprocess
DB_HOST = raw_input ('enter the host--> ')
DB_USER = raw_input ('enter the username--> ')
pswd = getpass.getpass('Password:')
fileName = raw_input ('enter the file to search-->')
result = subprocess.check_output('find /home/ayadav -name '+fileName+ '|wc -l', shell=True)
if int(result) == 1 :
        pass
	print 'Info: File exists at location'
	print 'File Count: '+result 
	FILE_NAME = subprocess.check_output(['/home/ayadav/alok_project/git.sh'])
	FILE = os.path.basename(FILE_NAME)
        NAME = os.path.splitext(FILE)[0]
        print FILE_NAME
elif int(result) > 1 :
	print 'Error: Multiple files found so shell exits'
	print 'File count: '+result
        exit()
else:
	print 'Error: File Count: '+result  
        print 'shell exits'
        exit()

DATETIME = time.strftime('%d-%m-%Y-%H-%M-%S')
DATE = time.strftime('-%d-%m-%Y')
def singledatabase():
    while True:
            DB_NAME=raw_input("enter the database name--> ")
            print "Executing patch in database " +DB_NAME
            result = subprocess.call('mysql -u' + DB_USER + ' -p' + pswd + ' -h' + DB_HOST + ' -vvv ' + DB_NAME + ' < ' + FILE_NAME, shell=True)
            if result == 0:
                    p = subprocess.call(["/home/ayadav/alok_project/sql.sh", DB_NAME, DB_HOST, FILE ], shell = False)
                    print ("database dump restored")
                    while True:
                            s = raw_input("enter yes if you want to continue else no-->")
                            if s == 'no':
                                   return False
                            elif s == 'yes':
                                   return singledatabase()
                                   print 'restarting'
                            else:
                                print("you entered wrong choice Please enter corrrect response")
                                continue
            
            else:
                logging.error("databases did not dump; result code: %d" % result)
                return False

def allshard():
    list=['shard1001','shard1002','shard1003','shard1004','shard1005']
    for DB_NAME in list:
                      print "Executing patch in database " +DB_NAME
                      result = subprocess.call('mysql -u' + DB_USER + ' -p' + pswd + ' -h' + DB_HOST + ' -vvv ' + DB_NAME + ' < ' + FILE_NAME, shell=True)
                      if result == 0:
                              p = subprocess.call(["/home/ayadav/alok_project/sql.sh", DB_NAME, DB_HOST, FILE ], shell = False)
                              print ("database dump restored")
                      else:
                          logging.error("databases did not dump; result code: %d" % result)

def allshard_as():
    list_as=['shard1001_as','shard1002_as','shard1003_as','shard1004_as','shard1005_as']
    for DB_NAME in list_as:
        print "Executing patch in database " +DB_NAME
        result = subprocess.call('mysql -u' + DB_USER + ' -p' + pswd + ' -h' + DB_HOST + ' -vvv ' + DB_NAME + ' < ' + FILE_NAME, shell=True)
        if result == 0:
                 p = subprocess.call(["/home/ayadav/alok_project/sql.sh", DB_NAME, DB_HOST, FILE ], shell = False)
                 print ("database dump restored")
        else:
            logging.error("database didnot dump; result code: %d" % result)


def none_database():
    dumpcmd = "mysql -u" + DB_USER + " -p" + pswd + " -h" + DB_HOST + " -vvv " " < " + FILE_NAME + " >> " + NAME + DATE + ".txt"
    os.system(dumpcmd)
    print ('patch executed')

def errhandler ():
    print "Your input has not been recognised"

takeaction = {
    "1": singledatabase,
    "2": allshard,
    "3": allshard_as,
    "4": none_database,
    }
alok = raw_input("Please enter 1.for executing in single shard 2. for allshard 3. for allshard_as 4. for none  ")
takeaction.get(alok,errhandler)()

