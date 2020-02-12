n = int(input())
l = []
for x in range(n):
    inp = int(input())
    if inp > 0:
        l.append(inp)
    else:
        l.pop()
counter = 0
for a in l:
    counter += a
print(counter)
