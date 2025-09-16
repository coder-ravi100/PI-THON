#CHECK WHETHER A PERSON IS ELIGIBLE FOR DRIVING (AGE >= 18 AND HAS_LICENSE)
'''
➡️ Program Name:
Check whether a person is eligible for driving

➡️ Input:
age (integer)
has_license (boolean → Yes/No ya True/False)

➡️ Output:
"Eligible for Driving" ya
"Not Eligible for Driving"

➡️ Logic (Step by Step):
Step 1 → Check karo ki age >= 18 hai ya nahi.
Step 2 → Agar age >= 18 hai to check karo has_license.
Step 3 → Agar dono condition true hai → print “Eligible”.
Step 4 → Agar koi bhi condition false hai → print “Not Eligible”.'''

age = int (input ("Enter The Age :"))

has_license = input("Do you have a license? (yes/no): ")

if age >= 18:

    if has_license == "yes":

        print(f"Eligible for Driving :{age}")

    else:

        print(f"Licence Must Have :{age}")

else:
    
    print(f"Not Eligible for Driving Your Age Is  :{age}")



