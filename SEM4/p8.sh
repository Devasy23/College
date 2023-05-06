echo "enter your choice"
echo "1) Head"
echo "2) Tail"
echo "3) Exit"
read n
until [ $n = 3 ]
do
case $n in
1) echo "Enter the numer of lines u want to print"
read pt
# echo "Enter the name of file"
# read f1
i=0
exec < f1;
while [ $i -lt $pt ]
do
read line;
echo $line;
i=`expr $i + 1`
done
;;
2) echo "Enter the numer of lines u want to print"
read pt
# echo "Enter the name of file"
# read f1
len=`cat f1 | wc -l`
i=1
v=`expr $len - $pt`
exec < f1
while [ $i -le $len ]
do
read line
if [ $i -gt $v ]
then 
echo $line
fi
i=`expr $i + 1`
done
;;
3)  echo "exited"
    exit
;;
esac
echo "enter your choice"
echo "1) Head"
echo "2) Tail"
echo "3) Exit"
read n
done