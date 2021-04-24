#Write a function that converts °C to °F.
def to_F(tem):
    f=32
    f= tem*1.8 + 32
    return f
print("Temp in c:")
c= float(input())
f = to_F(c)
print("Temp in faren:",f) 