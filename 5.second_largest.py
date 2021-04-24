#to determine the second largest numbers between 20 numbers
integers=[]
for i in range(20):
    integers.append(int(input()))
k = max(integers)
for i in integers:
    if(i == int(k)):
        integers.remove(i)
integers.remove(k)
l = max(integers)
print("2nd largest is :",l)

