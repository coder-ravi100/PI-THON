'''
RANGE FUNCTION IN USE
range() kyu likhte hai?

*Jab Hume repeat kaam karna ho (jaise counting, table, reverse counting, ya fixed steps me print karna), 
to manually number likhne ke bajaye range() automatically sequence banata hai.
Ye loop ko control karta hai:

*Kahan se start karna hai
*Kahan tak chalna hai
*Kitne step me aage ya peeche chalna hai

range(start, stop, step)

start → kahan se shuru karna hai (default = 0)
stop → kahan tak chalna hai (but stop wala number include nahi hota)
step → kitne-2 ya kitne-3 se badhaye/ghataye (default = 1)

'''

for _ in range(10): #VARIABLE KI JARURAT HI NAHI HAI ISS LIYE (_ UNDERSCORE KA USE KIYA HAI)
    print("Hello Word")
print("\n")#--------------------------------------------------------------------------------
for i in range (1,7): #1-start , 7-stop
    print("Bye Bye",i) #Har iteration me "Bye Bye" ke saath i ki current value print karega
print("\n")#--------------------------------------------------------------------------------
for i in range (1,10,3): #1-start 10-stop 3-step
    print("morning",i)
    '''
    range(start, stop, step) ka matlab:
    start = 1 → loop 1 se start hoga.
    stop = 10 → 10 tak chalega (10 include nahi hota).
    step = 3 → har baar i ki value 3-3 se badhegi.

    i ki values:
    Pehla: 1
    Next: 1 + 3 = 4
    Next: 4 + 3 = 7
    Next: 7 + 3 = 10 → lekin 10 include nahi hota, isliye loop yahin ruk jaayega.
    '''
print("\n")#--------------------------------------------------------------------------------
for i in range (10,1,-1):
    print(i)
'''
range(start, stop, step) explanation:
start = 10 → loop 10 se start hoga.
stop = 1 → 1 tak chalega (but 1 include nahi hota).
step = -1 → har baar i ki value 1-1 se kam hoti jayegi.

i ki values:
Pehla: 10
Next: 9
Next: 8
Next: 7
…
2 tak chalega.
1 pe loop ruk jaayega (kyunki stop exclude hota hai).
'''
print("\n")#--------------------------------------------------------------------------------
