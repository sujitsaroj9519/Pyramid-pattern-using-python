n = int(input())
for row in range(1, n):
    for column in range(row, 0, -1):
        print(column, end=" ")
    print("")