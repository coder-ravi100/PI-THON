
# FIND THE GREATEST AMONG THREE NUMBER 
num1 = int(input("Enter The Number 1 : "))
num2 = int(input("Enter The Number 2 : "))
num3 = int(input("Enter The Number 3 : "))

if num1 > num2 and num1 > num3:

    print(f"Biggest Number Is : {num1}")

elif num2 > num1 and num2 > num3:

    print(f"Biggest Number Is : {num2}")

else:

    print(f"Biggest Number Is : {num3}")
