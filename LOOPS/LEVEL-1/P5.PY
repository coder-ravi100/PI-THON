#PRINT SUM OF EVEN AND ODD NUMBER 1 TO 'N'
'''
num = 10
Even = 2 4 6 8 10
Odd = 1 3 5 7 9
sum of even No : 30
Sum of Odd No : 25
'''
num = int (input("Enter The Number :"))

i = 1
sum_even = 0
sum_odd = 0
for i in range (i,1+num,+1):
    
    if (i % 2 == 0):
        sum_even += i
        print(i,"Even")
    else:
        sum_odd += i
        print(i,"Odd")
        
    
print(f"Sum Of Even Number :{sum_even}")
print(f"Sum Of Odd Number :{sum_odd}")
