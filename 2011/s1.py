N = int(input())
val = []
for x in range(N):
    val.append(input())
counterT = 0
counterS = 0
for items in val:
    counterT += items.count('T') + items.count('t')
    counterS += items.count('S') + items.count('s')

if counterT > counterS:
    print('English')
elif counterT < counterS or counterT == counterS:
    print('French')
