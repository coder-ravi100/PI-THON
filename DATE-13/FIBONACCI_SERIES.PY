# Fibonacci Series in Python

# term = int(input("Enter the terms = "))  

# n1, n2 = 0, 1
# print("Fibonacci series =", n1, n2, end=" ")

# for i in range(1, term - 1):  
#     n3 = n1 + n2
#     print(n3, end=" ")
#     n1 = n2
#     n2 = n3


term = int(input("Enter The Terms = "))

n1, n2 = 0, 1
print("Fibonacci Series =", n1, n2, end=" ")

count = 2   

while count < term:
    n3 = n1 + n2
    print(n3, end=" ")
    n1 = n2
    n2 = n3
    count += 1


