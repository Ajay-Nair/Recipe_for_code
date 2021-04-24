#to calculate average of ten numbers
x=[]
for i in range(10):
    x.append(int(input()))
s=0
for i in x:
    s = s + i
print(s/10)
