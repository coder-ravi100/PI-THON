#PRINT Q 1 TO 'N' NUMBER USE IN BOTH LOOP WHILE AND FOR
num = int (input ("Enter The Number :"))
i = 1
while num >= i:
    print(i)
    i+=1
'''
Enter :100 
1 to 100
'''
print("\n")
starting = int (input("Enter The Value :"))
for i in range (1,starting,1):
    print(i)