# Write operations to implement multiply, subtract, and divide operations using only addition. The results
# are all integers and so are the operands..


def mult(a, b):
    total = 0
    for i in range(0, b):
        total += a
    return total

def div(a, b):
    total = 0
    dividend = 0
    isNegative = False
    if a < 0:
        a = a * -1
        isNegative = True
    while dividend <= a:
        dividend += b
        total += 1 if dividend <= a else 0
    if isNegative:
        total *= -1
    return total

def sub(a, b):
    return a + -b

print("2 * 5", mult(2, 5))
print("20 / 3", div(20, 3))
print("5 - 2", sub(5, 2))
print("-21 / 7", div(-21, 7))
