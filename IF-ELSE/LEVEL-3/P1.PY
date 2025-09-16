#LEVEL-3:ELSE - IF LADDER
#FIND GRADE BASE ON MARK
'''
|*90+ = A| |80+ = B| |70+ = C| |60+ = D| |ELIF = FAIL|
'''
marks = int (input ("Enter The Number :"))

if marks  >= 90:
    print(f"Grade A {marks}")
elif marks >= 80:
    print(f"Grade B {marks}")
elif marks >= 70:
    print(f"Grade C {marks}")
elif marks >= 60:
    print(f"Grade D {marks}")
else:
    print(f"Fail {marks}")
