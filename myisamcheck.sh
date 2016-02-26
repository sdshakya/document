#!/bin/sh
export EMAIL_RECIPIENT1=jrick@deerwalk.com,rwoollam@deerwalk.com,aranjan@deerwalk.com,aswar@deerwalk.com,sdshakya@deerwalk.com,_re@deerwalk.com
#export MYISAM_DIR=/mnt/_$(date +"%m-%Y")
export LOGFILE=/backup/myisamcheck/myisam_$(date +"%d-%m-%Y").log
mysql -uroot -pmuljara -e "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'usermanagement' AND ENGINE LIKE '%MyISAM%';" > $LOGFILE
#cat $LOGFILE | mail -s "MYISAM Table Report For Usermanagement ClientUAT In 10.0.44.223  As Of $(date +'%m-%d-%Y')" $EMAIL_RECIPIENT1
mycount=`cat $LOGFILE | wc -l`
if [ $mycount -eq 0 ]
then
 echo "No MYISAM tables in the list" > $LOGFILE
cat $LOGFILE | mail -s "MYISAM Table Report For Usermanagement Client UAT In 10.0.44.223  As Of $(date +'%m-%d-%Y')" $EMAIL_RECIPIENT1
else
cat $LOGFILE | mail -s "MYISAM Table Report For Usermanagement Client UAT In 10.0.44.223  As Of $(date +'%m-%d-%Y')" $EMAIL_RECIPIENT1
fi
