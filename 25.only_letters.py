#Check if a text file contains only letters.
Flag = 0
f = open("Hello World.txt","r")
lst = []
a =f.read()
for i in a :
    lst.append(i.strip())
for j in lst:
    if(j == ''):
        lst.remove('')
for letter in lst:
    if(letter.isalpha()==False):
        Flag =1
        break
if(Flag==1):
    print("No")
else:
    print("Yes")
print(lst)