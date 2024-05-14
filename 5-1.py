# Insertion
# Given two 32 bit numbers N and M, write a method to instert M into N given two positions i and j
# Example, N = 10000000000 M = 10011 i = 2 j = 6
# Output: N = 10001001100
# Assume M can fit between i and j

n = 0b10000000000
m = 0b10011
i = 2
j = 6

allOnes = ~0
left = allOnes << (j + 1)
right = (1 << i) - 1
mask = left | right

n_cleared = n & mask
print(n_cleared, bin(n_cleared))
print(bin(m << i))
n_m = n_cleared | (m << i)
print(n_m)
print("Expected", 0b10001001100)

