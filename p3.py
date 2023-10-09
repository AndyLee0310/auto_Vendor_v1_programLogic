def group(n):
    result = 0
    for i in range(1, n + 1):
        if i % 3 != 0:
            result += 1
    return result

n = int(input())
print(group(n))