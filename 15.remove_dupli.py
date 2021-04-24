# Remove duplicates from a list of numbers.
num = [1,2,3,4,4,5,6,6,7,7,7,8,9,12,8]
req_num=[]
size = len(num)
for i in num:
    if i not in req_num:
        req_num.append(i)
print(req_num)
