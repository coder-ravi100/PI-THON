#prime NUMBER (1 TO 100) 
#USING WHILE

num = int (input ("Enter The Number :")) #11

i = 2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
flag = 1  

while i < num: #11 True
    if (num % i == 0):
        # flag = 0
        print("The Number Is Not Prime")
        break
    i+=1

if (flag == 1):
    print(f"Prime Number :{num}")
else:
    {
        print(f"Not Prime Number :{num}")
    }
  