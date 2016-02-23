#!/bin/bash

echo "file name"
read path
 
count=`s3cmd ls s3://dw-build/$path | wc -l`

if test ${count} -ne 0
then
        echo "exist"
else
        echo "do not exist"
fi
