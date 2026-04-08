word1 = "abc"
word2 = "pq"
output = ""
if len(word1)<=len(word2):
    length = len(word1)
else:
    length = len(word2)

for i in range(length):
    output+=(word1[i]+word2[i])

if len(word1)<=len(word2):
    output+=(word2[len(word1):])
else:
    output+=(word1[len(word2):])

print(output)


#Question 2

s = "abcd"
t = "abcde"

for char in t:
    if t.count(char) > s.count(char):   # If I were have known about the count function of python, this would have been easier. I need more strings functions.
        print(char)
        break
