# FIND CHARARACTER LOWERCASE OR UPPERCASE
chs=input("enter your character")
for ch in chs:
    if "a"<=ch<="z":
        print("lowercase")
    if "A"<=ch<="Z":
        print("uppercase")
print(ch)