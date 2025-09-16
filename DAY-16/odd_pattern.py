rows = int (input ("Enter The Number :"))

# rows = 5
for i in range(1, rows+1):
    num = 2*i - 1      # odd number
    for j in range(i): # print i times
        print(num, end=" ")
    print()            # new line after each row

    '''
    how to work program

    num = 2 * i - 1 
    1   = 2 * 1 - 1 --> 1
    3   = 2 * 2 - 1 --> 3 3 
    5   = 2 * 3 - 1 --> 5 5 5
    7   = 2 * 4 - 1 --> 7 7 7 7
    9   = 2 * 5 - 1 --> 9 9 9 9 9

    '''
