# FIND CHARARACTER LOWERCASE OR UPPERCASE
def ques1():
    chs=input("enter your character: ")
    for ch in chs:
        if "a"<=ch<="z":
            print("lowercase")
        if "A"<=ch<="Z":
            print("uppercase")
    print(ch)


#Sum of N numbers
def ques2():
    n=int(input("Enter your number: "))
    sum=0
    for i in range(1,n+1):
        sum+=i
    print(sum)


#Sum of odd numbers
def ques3():
    n=int(input("enter your number: "))
    sum=0
    for i in range(1,n+1,2):
        sum+=i
    print(sum)


#check number is prime or not 
def ques4():
    n=int(input("enter your number"))
    prime=True
    if n<2:
        prime=False
    while n>2:

#sum of digit of input number
#number of digit in a number