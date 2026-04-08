# 28. Find the Index of the First Occurrence in a String



haystack = "mississippi"
needle = "issip"

if needle not in haystack:
    print(False)

count=0
for char in haystack:

    if needle[0] == char:
        print(char)
        index_start = count
        print(index_start)
        # Extract the substring.
        index_end = index_start + len(needle)
        print(haystack[index_start:index_end])
        if haystack[index_start: index_end] == needle:
            print(index_start)
    count+=1

#242. Valid Anagram
s = "anagtam"
t = "nbgbram"
is_anagram = False
for char in t:
    if (t.count(char) == s.count(char)) and (len(s) == len(t)):
        is_anagram = True
    else:
        is_anagram = False
        break
    if (t.count(char) == s.count(char)) and (len(s) == len(t)):
        is_anagram = True
    else:
        is_anagram = False
        break
print(is_anagram)



