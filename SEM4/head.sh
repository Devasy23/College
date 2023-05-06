pt=$1;
i=0
exec < f1.txt;
while [ $i -lt $pt ]
do
read line;
echo $line;
i=`expr $i + 1`
done