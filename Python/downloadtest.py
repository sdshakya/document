import os
import subprocess
import getpass


fileName = raw_input('Enter File Name To Be restored: ')
user = raw_input('Enter Your User Name: ')
database = raw_input('Enter DB name: ')
host = raw_input('Enter Host Name: ')
password = getpass.getpass("Password will not be visible:")
dbfilename = raw_input()
result = subprocess.check_output('s3cmd ls s3://dw-build/'+fileName+ '|wc -l', shell=True)
if int(result) == 1 :
	print 'Info: File exists in S3 Bucket'
	print 'File Count: '+result 
	command = 's3cmd get s3://dw-build/'+fileName
	get = os.system(command)
	if get == 0:
		print'File Downloaded Successfully'
		print 'Restore is in progress'
		restore = subprocess.check_output("mysql -u%s -p%s -h%s %s < %s.sql" % (user,password,host,database,dbfilename))	
		if int(restore) == 1 :
			print 'Restore is completed.'
		else:
			print 'Restore failed'
			
	else:
		print'Download Failed'
	
elif int(result) > 1 :
	print 'Error: Multiple files found'
	print 'File count: '+result
else:
	print 'Error: File Count: '+result

