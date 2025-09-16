#SUM OF DIGITS
'''
NUM = 123 
SUM OF DIGITS = 1+2+3 = 6
'''
num = 125
digits = 0
digits_sum = 0

while num != 0:
    num = num // 10
    digits+=1
    digits_sum =  digits + digits

print(f"Total Digits : {digits}")
print(f"Sum Of Digits: {digits_sum}")

