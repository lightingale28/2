a=int(input("please enter your first side length: "))
b=int(input("please enter your second side length: "))
c=int(input("please enter your third  side length: "))
if c>a+b or a>b+c or b>a+c:
    print("no")
elif a==0 or b==0 or c==0 :
    print("length can't be 0")
else:
    print("yes")
