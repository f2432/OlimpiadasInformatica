n,q = list(map(int, input().split()))
x = list(map(int, input().split()))
intervalos = []
for i in range(q):
    intervalos.append(list(map(int, input().split())))
for set in intervalos:
    count = 0
    for j in x:
        if j >= set[0] and j<= set[1]:
            count += 1
    print(count)