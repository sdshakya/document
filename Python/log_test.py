import os
import subprocess
import getpass
import tarfile
import logging

#Take the input for DB restore
user = raw_input('Enter Your User Name: ')
password = getpass.getpass("Password will not be visible:")
host = raw_input('Enter Host Name: ')
database = raw_input('Enter DB name: ')
dbfilename = raw_input('Enter File Name To Be restored: ')

#log file name
LOG_FILENAME = 'DB_restore.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

#Download from S3 Bucket

result = subprocess.check_output('s3cmd ls s3://dw-build/'+dbfilename+ '|wc -l', shell=True)

#Checks is Download is complete or not
if int(result) == 1 :
	print 'Info: File exists in S3 Bucket'
	logging.debug('Info: File exists in S3 Bucket')
	print 'File Count: '+result 
	logging.debug('Info: File Count: '+result)
	command = 's3cmd get s3://dw-build/'+dbfilename
	get = os.system(command)

	if get == 0:
		print'File Downloaded Successfully'
		logging.debug('File Downloaded Successfully')
		
#Extraction Process Begins here
		print 'File extraction is in process'
		logging.debug('File extraction is in process')
		extract = subprocess.check_output('tar -zxvf ' +dbfilename, shell=True)
		File = dbfilename.split('.')
		sqlfile = extract.split('.')
		print extract
		#if extract == 0:
		#	print 'Extraction is complete'
		#else:
		#	print'Extraction Failed'

#compares zip file and extracted file name		
		if File[0] == sqlfile[0]:
			print 'Extraction complete'
			logging.debug('Extraction complete')
		else:
			print 'Extraction Failed'
			logging.debug('Extraction Failed')	
#restore process Begins here		
		print 'Restore is in progress'
		logging.debug('Restore is in progress')
		restore = subprocess.call('mysql -u' + user + ' -p' + password + ' -h' + host + ' ' + database + ' < ' + extract, shell=True)
		print restore
		if restore == 0:
			print 'Restore Completed'
			logging.debug('Restore Completed')
		else:
			print 'Restore Failed'	
			logging.debug('Restore Failed')
			
	else:
		print'Download Failed'
		logging.debug('Download Failed')
#Exception for multiple files	
elif int(result) > 1 :
	print 'Error: Multiple files found'
	logging.debug('Error: Multiple files found')
	print 'File count: '+result
	logging.debug('File count: '+result)
#If no file found
else:
	print 'Error: File Count: '+result
	logging.debug('Error: File count: '+result)
	

