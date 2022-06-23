if [ 101 -gt 100 ]
then
    echo "101 is greater than 100"
fi

echo "Please enter your name and press enter"
read inputname

echo "Hello ${inputname}"

echo "Enter 3 names separated with spaces"
read inputnames
personnumber=1

for i in $inputnames
do
    echo "Person number ${personnumber}: ${i}"
    ((personnumber++))
done