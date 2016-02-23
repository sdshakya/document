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
logging.basicConfig(level=logging.INFO, 
                    filename='DB_restore.log', # log to this file
                    format='%(asctime)s %(message)s') # include timestamp

#Download from S3 Bucket

check_file = subprocess.check_output('s3cmd ls s3://dw-build/'+dbfilename+ '|wc -l', shell=True)

#Checks is Download is complete or not

if int(check_file) == 1 :
	print 'Info: File exists in S3 Bucket'
	logging.info('Info: File exists in S3 Bucket')
	print 'Info: File Count: '+check_file 
	logging.info('Info: File Count: '+check_file)
	download_file = 's3cmd get s3://dw-build/'+dbfilename
	get = os.system(download_file)
	print 'Info: Download is in progress'
	logging.info('Info: Download is in progress')
	if get == 0:
		print'Info: File Downloaded Successfully'
		logging.info('Info: File Downloaded Successfully')
		
#Extraction Process Begins here
		print 'File extraction is in process'
		logging.info('Info: File extraction is in process')
		extract = subprocess.check_output('tar -zxvf ' +dbfilename, shell=True)
		File = dbfilename.split('.')
		sqlfile = extract.split('.')
		print extract
#compares zip file and extracted file name		
		if File[0] == sqlfile[0]:
			print 'Extraction complete'
			logging.info('Info: Extraction complete')
			delete_gz_file = subprocess.call('rm -rf '+dbfilename, shell=True)
			logging.info('Info: tar.gz file has been deleted after extraction')	
		else:
			print 'Extraction Failed'
			logging.info('Error: Extraction Failed')	
#restore process Begins here		
		print 'Restore is in progress'
		logging.info('Info: Restore is in progress')
		restore = subprocess.call('mysql -u' + user + ' -p' + password + ' -h' + host + ' ' + database + ' < ' + extract, shell=True)
		print restore
		if restore == 0:
			print 'Restore Completed'
			logging.info('Info: Restore Completed')
			delete_gz_file = subprocess.call('rm -rf '+extract, shell=True)
			logging.info('Info: sql has been deleted from the server')
		else:
			print 'Restore Failed'	
			logging.info('Error: Restore Failed')
			
	else:
		print'Download Failed'
		logging.info('Error: Download Failed')
#Exception for multiple files	
elif int(check_file) > 1 :
	print 'Error: Multiple files found'
	logging.info('Warning: Multiple files found')
	print 'File count: '+check_file
	logging.debug('Error: File count: '+check_file)
#If no file found
else:
	print 'Error: File Count: '+check_file
	logging.info('Error: File count: '+check_file)
	

