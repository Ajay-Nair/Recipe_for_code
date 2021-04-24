#To print number of vowels in a string
vowels=["a","e","i","o","u"]
print("Enter string:")
string = input()
count=0
for i in string:
    for j in vowels:
        if(i==j):
            count=count+1
print("The number of vowels:",count)