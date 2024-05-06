# Hop either 1 2 or 3 steps up N steps, how many paths are there?

def count_steps(n, memo):
    if memo[n] != 0:
        return memo[n]
    return count_steps(n - 1, memo) + count_steps(n - 2, memo) + count_steps(n - 3, memo)

def count(n):
    memo = [0 for i in range(n + 1)]
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2
    memo[3] = 4
    if memo[n] == 0:
        memo[n] = count_steps(n - 1, memo) + count_steps(n - 2, memo) + count_steps(n - 3, memo)
    return memo[n]



# 5 steps
# 4 - 3 - 2
# 3/2/1 - 2/1/0 - 1/0
# 2/1/0 - 1/0 - 0 -- 1/0 - 0 -- 0
# 1/0 - 0 -- 0 -- 0
# 0
# 13 paths

# 3 steps
# 2 - 1 - 0
# 1/0 - 0
# 0 
# 4 paths

# 2 steps
# 1/0
# 0
# 2 paths

# 1 step
# 0 
# 1 path

# 0 step
# 1 path (do nothing)


print(count(5))
