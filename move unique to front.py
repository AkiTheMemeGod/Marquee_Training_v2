from collections import Counter
x = list(map(int, input().split()))
x.append(-1)
c = Counter(x)
for k,v in c.items():
    if v > 1:
        for i in range(v-1):
            x.remove(k)
        x.extend([k]*(v-1))

print(x)
print("No of unique elements: ", len(x[:x.index(-1 )]))

