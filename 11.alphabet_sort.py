#Sort a list of strings alphabetically.

words =["Ajay","Abhay","bat","cat"]
temp = []
for i in words:
    temp.append(i)
sorted_words=[]
for i in range(len(temp)):
    smallest_word = min(temp)
    sorted_words.append(smallest_word)
    temp.remove(smallest_word)
print(words)
print("The sorted list is:")
print(sorted_words)
