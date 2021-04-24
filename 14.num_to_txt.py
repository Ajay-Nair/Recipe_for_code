#Convert a given number to its text equivalent.
num = input()
size = len(num)

#ONES PLACE
ones_dict = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine"
}
teen_dict = {
    "11" : "eleven",
    "12" : "twelve",
    "13" : "thirteen",
    "14" : "fourteen",
    "15" : "fifteen",
    "16" : "sixteen",
    "17" : "seventeen",
    "18" : "eighteen",
    "19" : "nineteen"
}
tens_dict = {
    "2" : "twenty",
    "3" : "thirty",
    "4" : "forty",
    "5" : "fifty",
    "6" : "sixty",
    "7" : "seventy",
    "8" : "eighty",
    "9" : "ninety",

}

if(size==1):
    print(ones_dict[num])
elif(size == 2 and num[0]=="1"):
    print(teen_dict[num])
elif(size == 2 and num[1] == "0"):
    print(tens_dict[num[0]])
elif(size == 2 ):
    print(tens_dict[num[0]],ones_dict[num[1]])
else:
    print("Size too big")

