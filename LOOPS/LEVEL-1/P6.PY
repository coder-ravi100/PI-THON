#PRINT SQUARE OF 1 TO N NUMBERS
'''
Square Logic
Num = 10
 1^1
 2^2
 3^3
 4^4
 5^5 
 6^6
 7^7
 8^8
 9^9
 10^10
 sum = xyz
'''
num = int(input("Enter The Number : "))
i = 1
square = 0
for i in range (i,num,+1):#Yaha loop i se shuru hoga aur num tak chalega (num exclude hota hai).

#for i in range (i,num+1) #Yaha loop i se shuru hoga aur num+1 tak chalega (num include hoga).
   square = i * i   # 
   print(f"Square of {i} is : {square}")
