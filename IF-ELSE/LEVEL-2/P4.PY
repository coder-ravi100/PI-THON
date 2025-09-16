#CHECK WHETHER A YESR IS LEAP YEAR OR NOT
year = int(input("Enter The Number : "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):

    print(f"Leap Year : {year}")

else:
    
    print(f"Not Leap Year : {year}")
