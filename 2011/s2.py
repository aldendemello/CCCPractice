n = int(input())
x = []
for y in range(n*2):
    x.append(input())
counter = 0
for z in range(n):
    if x[z] == x[z+n]:
        counter += 1
    else:
        pass
print(counter)
