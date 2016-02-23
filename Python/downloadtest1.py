import os
import subprocess
import getpass

user = raw_input('Enter Your User Name: ')
password = getpass.getpass("Password will not be visible:")
host = raw_input('Enter Host Name: ')
database = raw_input('Enter DB name: ')
dbfilename = raw_input('Enter File Name To Be restored: ')

result = subprocess.check_output('s3cmd ls s3://dw-build/'+dbfilename+ '|wc -l', shell=True)
if int(result) == 1 :
	print 'Info: File exists in S3 Bucket'
	print 'File Count: '+result 
	command = 's3cmd get s3://dw-build/'+dbfilename
	get = os.system(command)
	if get == 0:
		print'File Downloaded Successfully'
		print 'Restore is in progress'
		restore = subprocess.call('mysql -u' + user + ' -p' + password + ' -h' + host + ' ' + database + ' < ' + dbfilename, shell=True)
		print restore
		if restore == 0:
			print 'Restore Completed'
		else:
			print 'Restore Failed'	
			
	else:
		print'Download Failed'
	
elif int(result) > 1 :
	print 'Error: Multiple files found'
	print 'File count: '+result
else:
	print 'Error: File Count: '+result

