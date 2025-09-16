#CHECK PRIME NUMBER
num = int (input ("Enter The Number :"))
flag = 1
i = 1
while (i <= num):
    if (num % i == 0):
        flag = 1
    i+=1

if (flag == 1):
    print(num,"Is a Prime Number")
else:
    print(num,"Is a Not Prime Number")