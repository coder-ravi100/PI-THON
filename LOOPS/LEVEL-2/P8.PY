#CHECK FIBONACCI SERIES (FIRST N TERMS)

term = int(input("Enter The Term: "))

n1 = 0
n2 = 1
i = 1

print("\nFibonacci Series:", end=" ")
print(n1, n2, end=" ")   # first two terms

while i <= term - 2:
    n3 = n1 + n2
    print(n3, end=" ")   # print in same line
    n1 = n2
    n2 = n3
    i += 1
