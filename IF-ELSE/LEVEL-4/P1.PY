#LEVEL-4: NESTED IF - ELSE
#CHECK WHETHER A NUMBER IS POSITIVE NEGITIVE OR ZERO

num = int(input("Enter The Number : "))

if num >= 0: #positive hai ki nahi
    if num == 0: #check kiya ki zero hai ki nahi
        print("ZERO")
    else:
        print("POSITIVE")
else:
    print("NEGATIVE")
