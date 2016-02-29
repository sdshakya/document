#!/bin/bash
rm /tmp/processlist.txt
rm /tmp/outlog.txt
/usr/bin/mysql -uroot -pmuljara -e "SELECT CONCAT('KILL ', id,';') FROM information_schema.PROCESSLIST WHERE Command='sleep' INTO OUTFILE '/tmp/processlist.txt';" -vv > /tmp/outlog.txt
/bin/cat /tmp/outlog.txt

/usr/bin/mysql -uroot -pmuljara -e "source /tmp/processlist.txt;" -vv > /tmp/outlog.txt
/bin/cat /tmp/outlog.txt

TOTALPROCESS="$(/bin/cat /tmp/processlist.txt | wc -l)"
echo ">>>>>>>>>>>>>>>>>>>>>> $TOTALPROCESS SLEEP PROCESSES WERE KILLED <<<<<<<<<<<<<<<<<<<<<<<<<<"

/bin/rm -f /tmp/processlist.txt /tmp/outlog.txt

