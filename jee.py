n = int(input("Enter number of visits: "))
r = list(map(int, input("Enter ranks: ").split()))
min_rank = r[0]
c = 0
for i in range(1, n):
    if r[i] < min_rank:
        min_rank = r[i]
        c += 1
print("Number of cuts:", c)
