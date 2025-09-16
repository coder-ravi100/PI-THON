'''
1.COUNT EVEN AND ODD NUMBERS FROM GIVEN RANGE + SUM ALL NUMBER
EVEN - 2 4 6 8 10
ODD - 1 3 5 7 9
NUM = 10
ODD = 1 EVEV = 2 ODD = 3 EVEN = 4 ODD = 5 EVEN = 6 ODD = 7 EVEN = 8 ODD = 9 EVEN = 10
SUM = ?
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