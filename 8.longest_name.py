print("Enter 10 names:")
names=[]
for i in range(10):
    names.append(input())
max=len(names[0])
k=0
for j in range(5):
    if(len(names[j])>max):
        max = len(names[j])
        k = j
print("The longest names are:")
for k in names:
    if(max == len(k)):
        print(k)