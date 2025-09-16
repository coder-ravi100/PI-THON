print("\nSkip For 4 Number")
for i in range (10):
    if i == 4:
        break
    print(i,end = " ")

print("\nSkip For 4 Number")
for j in range (10):
    if j == 4:
        print(j,end = " ")
        break

print("\nUsing While Loop Skip 4 Number")
i = 0
while i <= 10:
    print(i,end = " ")
    if i ==4:
        break
    i+=1


print("\nSkip 4 Number And Continue Next Number To Print")
for i in range (10):
    if i == 4:
        continue
    print(i,end =" ")

print("\nSkip 4 Number And Continue Next Number To Print")

for i in range (10):
    print(i,end = " ")
    if i == 4:
        continue
    
print("\nSkip 4 Number And Continue Next Number To Print")
for i in range (10):
    if i == 4:
        pass
    print(i,end = " ")
'''
Important Point:
pass ka use tab karte hain jab hume code likhna baaki ho,
ya condition me abhi kuch nahi karna hai.
Agar pass hata doge to bhi output same hi rahega.
'''
print()
for i in range (10):
    # if i == 4:
    #     pass
    print(i,end = " ")

i = 0
while i <=10:
    pass
