# class User:
#     pass
#
# user_1 = User()
# user_1_id = "001"
# user_1.username = "Luv"
# print(user_1.username)

# Adding constructor and attributes to a class
# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0  #This is the default value
#
# user_1 = User("01", "Luv")
# print(user_1.id)
# print(user_1.username)
# print(user_1.followers)

#Adding methods to a class


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  #This is the default value
        self.following = 0
        self.following_list = []
        self.followers_list = []

    def follow(self, user):
        user.followers+=1
        user.followers_list.append(user.id)
        self.following += 1
        self.following_list.append(user.id)

user_1 = User("01", "Luv")
user_2 = User("02", "Ratna")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_1.following_list)
print(user_2.followers)
print(user_2.following)
print(user_2.followers_list)















