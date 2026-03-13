import math
n,q = list(map(int, input().split()))
x = list(map(int, input().split()))
intervalos = []
for i in range(q):
    intervalos.append(list(map(int, input().split())))
x.sort()
def binSearch(list, ref, carry):
    if len(list) > 1:
        if list[math.floor(len(list)/2+1)] > ref:
            return binSearch(list[math.floor(len(list)/2+1):], ref, carry)
        else:
            return binSearch(list[:math.floor(len(list)/2+1)], ref, carry+len(list[math.floor(len(list)/2+1):]))
    else:
        return carry+1
def binSearchOver(list, ref, carry):
    if len(list) > 1:
        if list[math.ceil(len(list)/2+1)] >= ref:
            return binSearch(list[math.ceil(len(list)/2+1):], ref, carry)
        else:
            return binSearch(list[:math.ceil(len(list)/2+1)], ref, carry+len(list[math.ceil(len(list)/2+1):]))
    else:
        return carry+1
for set in intervalos:
    print(binSearchOver(x, set[1], 0) - binSearch(x, set[0], 0))
