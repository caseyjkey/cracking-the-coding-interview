# Write a method to find the maximum of two numbers without using if-else or any other comparison operator

def max(a, b):
    return (a + b) / 2 + abs(a - b) / 2

print(max(5,10))
print(max(10, 100))
