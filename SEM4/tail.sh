pt=$1
len=`cat f1.txt | wc -l`
i=1
v=`expr $len - $pt`
exec < f1.txt
while [ $i -le $len ]
do
read line
if [ $i -gt $v ]
then 
echo $line
fi
i=`expr $i + 1`
done