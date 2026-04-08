# #Traditional method of creating class and objects
# class Person:
#     name = "Luv"
#     occupation = "Machine Learning Quant"
#
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")
# a = Person()
# a.info()
# a.name = 'Ratna'
# a.occupation = 'IAS'
# a.info()


# Creating a class an object using a constructor

class Person:
    def __init__(self,name,occ): #This method will be invoked whenever I will create an object with this class
        # print("Hey I am a person")
        self.name = name
        self.occ = occ
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Luv", "Machine Learning Quant") #Self argument is automatically passed, we don't need to explicitly define it while creating ab object
b = Person("Ratna", "IAS")
c = Person(1,2)

a.info()
b.info()
c.info()

















