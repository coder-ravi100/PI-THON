# string = input("Enter The String : ")

# lower_str = string.lower()
# upper_str = string.upper()
# capitalized_str = string.capitalize()
# title_str = string.title()


# print("Lowercase   :", lower_str)
# print("Uppercase   :", upper_str)
# print("Capitalized :", capitalized_str)
# print("Title Case  :", title_str)

string = input("Enter The String : ")

for ch in string:   
    print("\nOriginal    :", ch)
    print("\nLowercase   :", ch.lower())
    print("\nUppercase   :", ch.upper())
    print("\nCapitalized :", ch.capitalize())
    print("\nTitle Case  :", ch.title())
    print("------------")

