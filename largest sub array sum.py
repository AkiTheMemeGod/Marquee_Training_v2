sums = set()
for i in range(len(x)):
    for j in range(i, len(x)):
        sums.add(sum(x[i:j+1]))
# print(sums.values())
print(max(sums))
