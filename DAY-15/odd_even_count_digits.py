#count no of even and odd digits from given number
'''
step 1:
koin sa number Even hai or Odd hai woh check karna hai

step 2: 
mile hue even or odd number ka digit kitane hai woh find karna hai

step 3:
ab even number ka sum or and kitane digits hai woh print karna hai
'''
num = int (input ("Enter The Number :"))
even_sum = 0
odd_sum = 0
i = 1
for i in range (i,num,+1):
    if (i % 2 == 0):
        print(f"Even :{i}")
        even_sum +=i
    else:
        print(f"Odd :{i}")
        odd_sum += i

print(f"Sum Of Even Number : {even_sum}")
print(f"Sum Of Odd Number : {odd_sum}")


