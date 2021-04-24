#Convert color Hex code to RGB code.
def toRGB(item):
    hex_dict = {
        "A" : 10,
        "B" : 11,
        "C" : 12,
        "D" : 13,
        "E" : 14,
        "F" : 15,
    }
    if(item[1].isalpha()==True):
        ones = hex_dict[item[1]]
    else:
        ones = item[1]
    
    if(item[0].isalpha()==True):
        tens = hex_dict[item[0]]
    else:
        tens = item[0]
    return 16*int(tens)+int(ones)



print("Input hex code")
hex = input()
hex = hex[1::]
r_hex = hex[0:2:]
g_hex = hex[2:4:]
b_hex = hex[4:6:]
R = toRGB(r_hex)
G = toRGB(g_hex)
B = toRGB(b_hex)
print(r_hex,g_hex,b_hex)
print(R,G,B)