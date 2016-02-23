import os
fileName = raw_input('Enter file name: ')
print 's3cmd put '+fileName+' s3://dw-build/'
command = 's3cmd put '+fileName+' s3://dw-build/'
os.system(command)
