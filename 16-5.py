# Write a program to find the number of trailing zeros for n factorial
n = 100
factorial = 1
for i in range(2, n + 1):
    factorial *= i
factorial = str(factorial)
answer = 0
while factorial[-1] == '0':
    answer += 1
    factorial = factorial[0:-1]
print(answer)
