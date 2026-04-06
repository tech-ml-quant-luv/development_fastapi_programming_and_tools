print("Hello World!")

with open("./data/madlibs.txt", "r") as file:
    data = file.read()
    print(data)

# print(type(data))
# print(data.find("<"))
#
# start_indexes = []
# end_indexes = []
# count = 0
# for i in data:
#     if i =="<":
#         start_indexes.append(count)
#     elif i ==">":
#         end_indexes.append(count)
#     count +=1
# print(start_indexes)
# print(end_indexes)


# Using Reverse two sum
current_char = 0
count = 0
for char in data:
    current_char = count
    text = ""
    if char == ">":
        while current_char >=0:
            text += data[current_char]

            if data[current_char] == "<":
                print(current_char, count)
                print(text[::-1])
                break
            current_char -=1

    count+=1






