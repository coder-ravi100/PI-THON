#COUNT DIGITS OF A NUMBERS
'''
step :1
num = 123

step :2
count Digits
Total Digit = 3
'''
num = int (input ("Enter The NUmber :"))
digit = 0

while num != 0:
    num = num // 10
    digit+=1

print(f"Total Digits :{digit}")



