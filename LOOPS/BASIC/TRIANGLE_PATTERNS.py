#TRIANGLE PATTERN
num1 = 5

for i in range (1+num1):
    for j in range (i): # 0 + 1 = 1 * ,1 + 2 = 3 ***
        print(" *",end=" ")
    print()

print("\n-----------------------")

num2 = 5

for i in range(1, num2 + 1):
    print(str(" *")* i)   # i ko i times repeat karna

print("\n------------------------")
num3 = 5

i = 1
while i <= num3:             #OUTER LOOP (ROW)
    j = 1
    while j <= i:           #INNER LOOP (COL)
        print("*",end = " ")
        j+=1
    print()                 #NEW LINE 
    i+=1
