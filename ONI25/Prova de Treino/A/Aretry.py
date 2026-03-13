t = int(input())
A=[]
N=[]
for _ in range(t):
    N.append(int(input()))
    A.append(list(map(int, input().split())))
printlist = []
for i in range(t):
    offset = 0
    prob = []
    for j in A[i]:
        if A[i][j-1] != j:
            offset += 1
            prob.append(j-1)
    if len(prob) > 2:
        printlist.append("NAO")
    else:
        if len(prob) == 0:
            printlist.append("SIM")
            continue
        if abs(prob[0]-prob[1]) == 1:
            printlist.append("SIM")
        else:
            printlist.append("NAO")
for str in printlist: #Actually printing
    print(str)