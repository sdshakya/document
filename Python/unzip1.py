import subprocess
import os.path
from subprocess import call
zipfile = input('file to be unzipped: ')
cmd='gunzip '+zipfile
statusResult, output1 = subprocess.getstatusoutput(cmd)
print (statusResult, output1)
if statusResult == 0:
	print ('success')
else:
	print ('failed')

		



