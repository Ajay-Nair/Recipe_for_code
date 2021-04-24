#Divide a number by 0 without seeing an error
a=10
b=0
try:
    z=a/b
    print(z)
except:
    z=b
    print(z)