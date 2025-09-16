#CHECK PALINDROME NUMBER
'''
pallindrome 
num = 153
'''
num = int (input ("Enter The Nunber :"))
rev = 0
rem = 0
temp = num

while num != 0:
    rem = num % 10
    rev = (rev * 10) + rem
    num = num // 10

if (rev == temp):
    print(temp,"Is a palindrome Number")
else:
    print(temp,"Is a Not palindrome Number")