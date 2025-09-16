#SIMPLE CALCULATOR
number1 = input("Enter Num 1 :")
number2 = input("Enter Num 2 :")
n1 = int (number1) #n1 = int(num1) ka matlab hai → user ke input ko string se integer me convert karke n1 me store karna.
n2 = int (number2)
add = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = float (n1) / float (n2) #Type Casting For Floating Value division
rem = float(n1) % float(n2) #Type Casting For Floating Value Modulures
print("\n")
print("Addition :",add)
print("Subtraction :",sub)
print("Multiplication :",mul)
print("Division :",div)
print("Remainder :",rem)  

