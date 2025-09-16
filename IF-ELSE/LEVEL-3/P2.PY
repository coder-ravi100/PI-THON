#CHECK WHETHER A CHARACTER IS VOWEL OR CONSONANT
ch = input("Enter The Character : ")

if (ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U' or
    ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
    print(f"Vowel Character : {ch}")
else:
    print(f"Consonant Character : {ch}")


# Short & Clean Version:
# Python me (in) operator use karna

# ch = input("Enter The Character : ")

# if ch in 'AEIOUaeiou':
#     print(f"Vowel Character : {ch}")
# else:
#     print(f"Consonant Character : {ch}")

