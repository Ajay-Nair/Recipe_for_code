#Write a function that takes a list of words and returns all the words that end with 'e'. 

def ends_e(list):
    print("Words that end with e are:")
    for i in list:
        l =len(i)
        if(i[l-1]=="e"):
            print(i)
    
print("Enter 5 words:")
words = []
for i in range(5):
    words.append(input())
ends_e(words)