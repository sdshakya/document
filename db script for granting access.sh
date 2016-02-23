#!/bin/bash
# bash script to create user in mysqldb 
echo "enter the choice 1.(for write access to user) 2.(for read only access) 3. (to change the password for user)-->"
read choice
case "$choice" in
      1) 
         echo "creating user for write access"
         read -p "Please enter the username you wish to create : " USER
         read -p "enter the password to that user :" PASS
         read -p "enter the database for access (*) for all or specify if any :" DATABASE
         read -p "enter the table for access (*) for all or specify if any :" TABLE
         read -p "enter the host for access % or localhost :" HOST
         mysql -uroot -p -hlocalhost <<EOF 
         create user '$USER'@'$HOST' identified by '$PASS';
         grant all privileges on $DATABASE.$TABLE to '$USER'@'$HOST';  
EOF
;;

      2)
         echo "creating user for read only access" 
         read -p "Please enter the username you wish to create : " USER
         read -p "enter the password to that user :" PASS
         read -p "enter the database for access (*) for all or specify if any :" DATABASE
         read -p "enter the table for access (*) for all or specify if any :" TABLE
         read -p "enter the host for access % or localhost :" HOST
         mysql -uroot -p -hlocalhost <<EOF
         create user '$USER'@'$HOST' identified by '$PASS';
         grant select on $DATABASE.$TABLE to '$USER'@'$HOST';   
EOF
;;


      3) 
         read -p "enter user_name to change the password :" USER
         read -p "enter the password for changing: " PASS
         read -p "enter the host % or localhost :" HOST
         echo "changing the password for user -->" $USER
         mysql -uroot -p -hlocalhost <<EOF
         SET PASSWORD FOR '$USER'@'$HOST' = PASSWORD('$PASS');
EOF
;;
 
      *)
         echo "wrong choice ! exiting " ;;
esac


