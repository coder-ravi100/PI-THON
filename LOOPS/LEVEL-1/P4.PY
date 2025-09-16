#PRINT TABLE OF 1 TO 'N' NUMBER (5 x 1 = 5...)
num = int (input ("Enter The Number :"))
'''
num = 5 
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
'''

for i in range (1,11,+1): 
    print(num , "X", i,"=", num*i)
    #loop Start Hoga 1 se aur 11 tak chala aur increment Hoga

counter = 1    
while counter <= 10:
    print(num , "X", counter,"=", num*counter)
    counter+=1