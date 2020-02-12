N = int(input())
swifts = list(input().split())
semaphores = list(input().split())
counter = []
swTotal = 0
semTotal = 0
for x in range(len(swifts)):
    swTotal += int(swifts[x])
    semTotal += int(semaphores[x])
    if swTotal == semTotal:
        counter.append(x+1)
    elif swTotal != semTotal:
        counter.append(0)
counter = set(counter)
print(max(counter))
