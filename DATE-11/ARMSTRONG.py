#WHAT IS A ARMSTRONG NUMBER
'''
An Armstrong number is a number that equals the sum of its own digits, 
each raised to the power of the total number of digits in the number. 
For example, 153 is an Armstrong number because it has three digits, 
and 1³ + 5³ + 3³ = 1 + 125 + 27 = 153. Another example is 8208, 
a four-digit number where 8⁴ + 2⁴ + 0⁴ + 8⁴ = 4096 + 16 + 0 + 4096 = 8208. 
'''
#ARMSTRONG NUMBER
num = int(input("Enter The Number : "))
digit = 0
sum = 0
rem = 0
temp = num
copy = num

# Count digits 
while num != 0:
    num = num // 10   # integer division
    digit += 1

# Armstrong check
while temp != 0:
    rem = temp % 10
    sum += rem ** digit
    temp //= 10

    print(f"Sum Number :{sum}")
if sum == copy:
    print(copy, "is an Armstrong Number")
else:
    print(copy, "is Not an Armstrong Number")
