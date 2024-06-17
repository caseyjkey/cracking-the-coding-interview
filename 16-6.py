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

l1 = sorted(a)
l2 = sorted(b)

i = j = 0
minimum = float('inf')
minPair = None

while i < len(l1) and j < len(l2):
    diff = l1[i] - l2[j]
    minPair = minPair if abs(diff) > minimum else (l1[i], l2[j])
    minimum = min(minimum, abs(diff))
    if diff < 0: # left is smaller than the right
        i += 1
    elif diff > 0:
        j += 1
    else:
        break

print(minimum, minPair)
