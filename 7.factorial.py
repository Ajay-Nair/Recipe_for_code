def fact(item):
    if(item!=0):
        item =item * fact(item-1)
        return item
    else:
        return 1
n = int(input())
k=fact(n)
print("Factorial of ",n,"is:",k)
