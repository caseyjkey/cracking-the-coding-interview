# Given two arrays of integers, find the two elements with the smallest difference
a = [121, 38, 8]
b = [7, 348, 12]

pair = None
smallestSum = float('inf')

for i in a:
    for j in b:
        if abs(i - j) < smallestSum:
            pair = (i, j)
            smallestSum = i - j

print(pair)
