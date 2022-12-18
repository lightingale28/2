"""#For a given input string “Python is a case sensitive language”. Write python code for the following:
a. Find the length of the input string.
b. Reverse the order of the string in one line code.
c. Using Slice function store “a case sensitive” in new string.
d. Replace “a case sensitive” with “object oriented”.
e. Find index of substring “a” in the given input string.
f. Remove the white spaces from the given input string."""
a="Python is a case sensitive language"
print(len(a))#a
print(a[::-1])#b
"""print(a.find("a case sensitive"))"""
print(a[10:26])#C
print(a.replace("a case sensitive","object oriented"))#d
print(a.index("a"))#e
print(a.replace(" ",""))#f