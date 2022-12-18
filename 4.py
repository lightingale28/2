"""Write a python program to find the greatest of three numbers entered by the 
user. """
n1 = int (input("Enter the 1st number: "))
n2 = int (input("Enter the 2nd number: "))
n3 = int (input("Enter the 3rd number: "))
if (n1 > n2):
    if (n1 > n3):
        print ("1st number is the largest number")
    else:
        print ("3rd number is the largest number")
elif (n2 > n3):
    print ("2nd number is the largest number")
else:
    print ("3rd number is the largest number")