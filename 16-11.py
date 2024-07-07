# You are building a diving board with boards of length "longer" and "shorter"
# Using K pieces of wood, how many different combinations can be made?

def perms(n: int) -> int:
    return 2**n

print(perms(3))

