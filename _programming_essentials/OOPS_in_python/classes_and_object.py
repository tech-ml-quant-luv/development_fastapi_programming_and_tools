class Person:
    name = "Luv"
    occupation = "Machine Learning Quant"
    networth = 10
    def info(self): #Self parameter is the reference to the current instance of the class and is used to access variables that belong o the class.
        print(f"{self.name} is a {self.occupation}")

a = Person() # This is an object of the Person Class
a.info()

#------------------------------------------------------

b = Person()
b.name = "Ratna"
b.occupation = "IAS"
b.info()
#-----------------------------------------------------


# print(a.name)
# print(a.occupation)
# a.name = "Ratna"
# a.occupation = "IAS"
# print(a.name, a.occupation)
#






