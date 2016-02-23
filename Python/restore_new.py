import os
import subprocess
import getpass

user = raw_input('Enter Your User Name: ')
password = getpass.getpass("Password will not be visible:")
host = raw_input('Enter Host Name: ')
database = raw_input('Enter DB name: ')
dbfilename = raw_input('Enter File Name To Be restored: ')

restore = subprocess.call('mysql -u' + user + ' -p' + password + ' -h' + host + ' ' + database + ' < ' + dbfilename, shell=True)

print restore
