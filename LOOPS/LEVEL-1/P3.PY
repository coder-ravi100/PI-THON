#PRINT EVEN AND ODD NUMBERS FROM  1 TO 'N'
'''
odd numbers are 3, 5, 7, 9, 11, 13, 15,…
even numbers are 2, 4, 6, 8, 10, 12, 14,…
'''
num = int (input ("Enter The Number :"))
i = 1
while (i <= num):
    if (i % 2 == 0):
        {
        print(f"Even :{i}")
        }
    else:
        {
        print(f"Odd :{i}")
        }
    i+=1

num = int (input ("Enter The Number :"))
i = 1
for i in range (i,num,+1):
    if (i % 2 == 0):
        {
            print(f"Even :{i}")
        }
    else:
        {
            print(f"Odd : {i}")
        }
'''
while loop 

while (num != 0)

{
        
}
'''



