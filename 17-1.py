# Write a function to add without using + or other arithmetic operators
# Hint, work through binary addition by hand
def Add(x, y):
    while (y != 0):
        carry = x & y
        x = x ^ y
        y = carry << 1
    
    return x

print(Add(11, 22))
