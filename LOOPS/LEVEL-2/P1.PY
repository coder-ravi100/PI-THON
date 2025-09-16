#REVERSE A NUMBER
'''
reverse number kya hai 
123 iss ka reverse 321 to ye hua reverse number

Correct Logic (Reverse a Number)
step 1:
num = 123
rev = 0
rem

Step 2:
Ek-ek digit nikalni hai rem = num % 10 se.
Reverse number ban na hai rev = rev * 10 + rem se.
Number ko chhota karna hai num = num // 10 se.
'''
num = 123
rev = 0
temp = num
# rev = 0
while (num != 0):
    rem = num % 10          #Yeh Code Last Digit Ko Nikalta Hai
    rev = rev * 10 + rem    # reverse number banaya    
    num = num // 10         # number ko chhota kiya         
num+=1

print(f"Normal No  :{temp}")
print(f"Reverse No :{rev}")

'''
DRY RUN CODE
REM = NUM(123) % 10
3   = 12       % 10
REM = NUM(12)  % 10
2   = 1        % 10
REM = NUM(1)   % 10
1   = 0        % 10
------------------
REV = REV * 10 + REM
13     0  * 10 +  3
REV = REV * 10 + REM
 12    1  * 10 + 2
REV = REV * 10 + REM
26     2  * 10 + 3
-----------------
num = num // 10
12    123 // 10
1     12 //  10
0     1  //  10



rev = 0
Take last digit 3 → rev = 0*10 + 3 = 3
Take last digit 2 → rev = 3*10 + 2 = 32
Take last digit 1 → rev = 32*10 + 1 = 321

'''