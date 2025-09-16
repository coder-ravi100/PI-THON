#CHECK STRONG NUMBER
num = int (input ("Enter The Number :"))
fact = 1
sum = 0
temp = num
#rem = 0
#i

while (num !=0):
    rem = num % 10

    fact = 1
    i = 1
    while (i <= rem):
        fact = fact * i
        i+=1
    sum = sum + fact
    num = num // 10

if (sum == temp):
    print (temp,"is a Strong Number")
else:
    print (temp,"is a Not Strong Number")
