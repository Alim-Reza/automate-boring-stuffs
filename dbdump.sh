DESKTOP_USER=
SERVER_PASSWORD=''
SERVER_PATH=
TIME=`date +%F`_`date +%r`
FILE_NAME=${TIME:0:19}
FILE_PATH=/home/$DESKTOP_USER/Documents/db_backup
DATABASE_USER_NAME=
DATABASE_NAME=
DATABASE_HOST=
DATABASE_PASSWORD=
FILE="$FILE_PATH/$FILE_NAME.sql"


#droping the local schema
echo "droping local schema....."
sudo -u postgres -H -- psql -d $DATABASE_NAME -c "DROP SCHEMA IF EXISTS skeleton CASCADE;"

#dumping from ***
echo "dumping from SERVER....."
sshpass -p $SERVER_PASSWORD ssh $SERVER_PATH "PGPASSWORD=$DATABASE_PASSWORD pg_dump -U $DATABASE_USER_NAME $DATABASE_NAME -h $DATABASE_HOST -C --column-inserts"  >> $FILE_PATH/$FILE_NAME.sql

sudo chmod a+rwx -R /home/$DESKTOP_USER/Documents/db_backup

#removing this line
# LINE="CREATE DATABASE ast WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';"
# echo 'Hello ' + $FILE
sed -i 's/CREATE DATABASE ast/---/g' ${FILE}

# #applying on local db
echo "applying on local db....."
sudo su - postgres -c "cat ${FILE} | psql ast"

echo "done."
