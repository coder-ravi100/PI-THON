#5.IDENTITY OPERATORS
'''
is → check memory location (object same hai ya nahi)
is not → check objects different
'''
#DOUBT TOOPIC
num1 = [1,2,3]

num2 = [1,2,3]

ans = num1

print(num1 == num2) #True

print(num1 is num2) #False

print(num1 is ans)  #True
