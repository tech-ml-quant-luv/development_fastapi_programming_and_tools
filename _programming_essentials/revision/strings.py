# print("My age: "+str(12))
# print(123+456)
# print(7-3)
# print(3*2)
# print(6/3)
# print(type(6/3))
# print(6//5) # This gives only the quotient
# print(type(6//3))
# print(2**3) #This means exponent
# print("Python uses the BODMAS also known as PEMDAS")
# print("Multiplication and division are on equal level and it depends on which one comes on the left most")
# print(3/3*3)

#Coding Exercise

weight = 69
height = 1.78

print(round(weight/(height **2),2))
score =100
score+=1
print(score)


###Project - Tip calculator

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10,12, or 15?"))
people = int(input("How many people to split the bill? "))
per_person = round((total_bill+(tip/100*total_bill))/people,2)

print(f"Each person should pay: ${per_person}")


print("This is a"+" " + "string")
print("""
This is a multi line string.
We can write in multiple lines.
It will not break.
""")
print()

print("String"[0])
print("String"[-1])
print("String"[-1:])
print("String"[:])
print("String"[2:])

#Looping through the strings

string = "Luv"

for characters in string:
    print(characters)

