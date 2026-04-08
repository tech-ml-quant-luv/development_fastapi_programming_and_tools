""" Basic numerical patterns """

user_input = 5
n = user_input+1
# for i in range(1,n):
#         print(f"{i}"*i)
# print()
# for i in range(1,n):
#     for j in range(1,i+1):
#         print(j, end="")
#     print()
# print()
#
# temp_n = n
# for i in range(1,n):
#     for j in range(temp_n,1,-1):
#         print(i, end="")
#     temp_n-=1
#     print()
#
# print()
#
# temp_n = n
# for i in range(1,n):
#     for j in range(temp_n,1,-1):
#         print(n, end="")
#     temp_n-=1
#     print()

"""# Star patterns from here"""
temp_n = n-1
for i in range(1,n):
    print("*"*temp_n)
    temp_n-=1
print()

temp_n = n-1
for i in range(1,n):
    print(" "*temp_n, end="")
    print("*"*i)
    temp_n-=1
