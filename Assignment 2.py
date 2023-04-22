# Question 1
a="python is a case sensitive language"
print("length of string=",len(a))
print(a[::-1])
b=a[10:26:1]
print(b)
replaced=a.replace("a case sensitive","object oriented")
print(replaced)
print(a.index("a"))
print(a.replace(" ",""))

#Question 2
name = "ABC"
SID = "2210XXXX"
department = "XYZ"
CGPA = 9.9
print("Hey,", name, "Here!\nMy SID is", SID, "\nI am from", department, "department and my CGPA is", CGPA)

#Question 3
a = 56
b = 10
print("a & b =", a&b)
print("a | b =", a|b)
print("a ^ b =", a^b)
print("Left shifting both a and b with 2 bits =", a<<2, "=", b<<2)
print("Right shifting a with 2 bits and b with 4 bits =", a>>2, "=", b<<4)

#Question 4
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
print("The greatest number of the three is", max(num1, num2, num3))

#Question 5
str = input("Enter the string: ")
if "name" in str:
    print("Yes")
else:
    print("No")

#Question 6
len1 = float(input("Enter length of side 1: "))
len2 = float(input("Enter length of side 2: "))
len3 = float(input("Enter length of side 3: "))
if len1 + len2 > len3 and len2 + len3 > len1 and len1 + len3 > len2:
    print("Yes")
else:
    print("No")