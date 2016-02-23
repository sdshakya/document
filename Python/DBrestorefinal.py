import os
import subprocess
import getpass
import tarfile
import logging
import os.path
from subprocess import call

#Take the input for DB restore
user = input('Enter Your User Name: ')
password = getpass.getpass("Password will not be visible:")
host = input('Enter Host Name: ')
database = input('Enter DB name: ')
dbfilename = input('Enter File Name To Be restored: ')

#log file name
logging.basicConfig(level=logging.INFO, 
                    filename='DB_restore.log', # log to this file
                    format='%(asctime)s %(message)s') # include timestamp

#Download from S3 Bucket

check_file, cmd = subprocess.getstatusoutput('s3cmd ls s3://dw-build/'+dbfilename)

#Checks is Download is complete or not

if check_file == 0 :
	print ('Info: File exists in S3 Bucket')
	logging.info('Info: File exists in S3 Bucket'+(str(check_file )))
	print ('Info: File Count: '+(str(check_file )))

	logging.info('Info: File Count: '+(str(check_file )))

	get = os.system('s3cmd get s3://dw-build/'+dbfilename)
	print ('Info: Download is in progress')
	logging.info('Info: Download is in progress')
	if get == 0:
		print('Info: File Downloaded Successfully')
		logging.info('Info: File Downloaded Successfully')
		
#Extraction Process Begins here
		print ('File extraction is in process')
		logging.info('Info: File extraction is in process')
		File = dbfilename.split('.')
		sql_filename = File[0]+'.'+File[1]
		print(sql_filename)
		statusResult, output1 = subprocess.getstatusoutput('gunzip '+dbfilename)
		print (statusResult, output1)
		if statusResult == 0:
			print ('success')
		else:
			print ('failed')
#==============================================================================
#compares zip file and extracted file name		
		#if File[0] == sqlfile[0]:
			#print ('Extraction complete')
			#logging.info('Info: Extraction complete')
			#delete_gz_file = subprocess.call('rm -rf '+dbfilename, shell=True)
			#logging.info('Info: gz file has been deleted after extraction')	
		#else:
			#print ('Extraction Failed')
			#logging.info('Error: Extraction Failed')	
#restore process Begins here		
		print ('Restore is in progress')
		logging.info('Info: Restore is in progress')
		restore, output2 = subprocess.getstatusoutput('mysql -u' + user + ' -p' + password + ' -h' + host + ' ' + database + ' < ' + sql_filename)
		print (restore)
		if restore == 0:
			print ('Restore Completed')
			logging.info('Info: Restore Completed')
			
		else:
			print ('Restore Failed'	)
			logging.info('Error: Restore Failed')
			
	else:
		print ('Download Failed')
		logging.info('Error: Download Failed')
#Exception for multiple files	
elif int(check_file) > 1 :
	print ('Error: Multiple files found')
	logging.info('Warning: Multiple files found')
	print ('File count: '+check_file)
	logging.debug('Error: File count: '+check_file)
#If no file found
else:
	print ('Error: File Count: '+check_file)
	logging.info('Error: File count: '+check_file)
	

