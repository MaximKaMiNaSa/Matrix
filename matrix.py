n = int(input())
m = int(input())

mult = []

for i in range(n):
    for j in range(m):
        mult.append([0]*m)

for i in range(n):
    for j in range(m):
        mult[i][j] = i * j

for x in range(n):
    print(*mult[x], sep=str().ljust(3))