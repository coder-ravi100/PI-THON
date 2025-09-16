#FIND THE LARGEST AMOUNG THREE NUMBERS USING NESTED IF :

num1 = int (input ("Enter The Number 1 :")) #20
num2 = int (input ("Enter The Number 2 :")) #10
num3 = int (input ("Enter The Number 3 :")) #13

if num1 > num2:

    if num1 > num3:

        print(f"BIGGEST NUMBER IS : {num1}")

    else:

        print(f"BIGGEST NUMBER IS : {num3}")

if num2 > num3:

    print(f"BIGGEST NUMBER IS :{num2}")

else:

    print(f"BIGGEST NUMBER IS :{num3}")

'''
Example (Largest of 3 Numbers)

Program Name: Largest of 3 Numbers

Input: num1, num2, num3

Output: Biggest Number

Logic:

Step 1: Compare num1 and num2

Step 2: Jo bada ho usko num3 se compare karo

Step 3: Jo sabse bada nikle use print karo

| num1 | num2 | num3 | Step1 (num1>num2?) | Step2 (winner>num3?) | Output |
| ---- | ---- | ---- | ------------------ | -------------------- | ------ |
| 20   | 10   | 13   | True (num1)        | True (num1>num3)     | 20     |

'''
