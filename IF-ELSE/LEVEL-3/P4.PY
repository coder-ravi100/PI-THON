#PRINT DAY OF WEEK BASE ON NUMBER (1-7)
day = int (input ("Enter The Number :"))

match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wensday")
    case 5: 
        print("Thuersday")
    case 6:
        print("FriDay")
    case 7:
        print("Satarday")
    case _:
        print("Invalid Day")