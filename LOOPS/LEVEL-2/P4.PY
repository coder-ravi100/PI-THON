#CHECK ARMSTRONG NUMBER
num = int (input ("Enter The Number :"))
digit = 0
sum = 0
#rem = 0
#power
temp = num 
copy = num

while (num !=0):
    num = num // 10
    digit+=1

while (temp !=0):
    rem = temp % 10
    power = rem ** digit
    sum = sum + power
    temp = temp // 10


if(sum == copy):
    print(copy,"Is a Armstrong Number")
else:
    print(copy,"Is a Not Armstrong Number")

