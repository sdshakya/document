import os
import subprocess

fileName = raw_input('Enter file name: ')
result = subprocess.check_output('s3cmd ls s3://dw-build/'+fileName+ '|wc -l', shell=True)
if int(result) == 1 :
	print 'Info: File exists in S3 Bucket'
	print 'File Count: '+result 
	command = 's3cmd get '+fileName+' s3://dw-build/'
	
elif int(result) > 1 :
	print 'Error: Multiple files found'
	print 'File count: '+result
else:
	print 'Error: File Count: '+result

