echo -n 'iniciando modo dev';
file1='/var/www/homeControl/homeControl.py'
file2='/var/www/homeControl.py'
cp $file1 $file2;
/var/www/homeControl/homeControl.fcgi &
last_id=$!;
date '+%H:%M:%S - ';
echo -n ejecutando nuevo proceso $last_id
while [ 1 ]
do
	if [ $file1 -nt $file2 ]
	then
		kill -9 $last_id > /dev/null;
		cp $file1 $file2; 
		/var/www/homeControl/homeControl.fcgi &
		date '+%H:%M:%S - ';
		last_id=$!;
		echo -n ejecutando nuevo proceso $last_id
	fi
	sleep 1;
done

