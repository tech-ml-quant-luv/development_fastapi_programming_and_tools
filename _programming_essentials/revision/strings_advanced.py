# String Slicing

print("Hello World")

name = "Luv, Ratan, Vaibhav, Suprit, Abhinav"
print(name[0:3])
print(len(name))

print(name[0:-3])
print(name[:-1:len(name)]) #This won't work
print(name[-3:-1])
print(name[-1:-3])  # This won't work as well
print("Harry"[-4:-2])
