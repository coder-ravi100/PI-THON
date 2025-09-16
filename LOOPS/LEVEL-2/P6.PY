#CHECK PERFECT NUMBER
num = int (input ("Enter The Number :"))
sum = 0
i = 1
while (i <= num):
    if (num % i == 0):
        sum = sum + i
    i+=1

if (sum == num):
    print(num,"Is a Perfect Number")

else:
    print(num,"Is a Perfect Number")

        