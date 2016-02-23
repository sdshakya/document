#!/usr/bin/env python

import os
import getpass
import time
import sys

fileName = raw_input('Enter file name: ')
command = 's3cmd get s3://dw-build/' + fileName
os.system(command)
