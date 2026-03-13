if int(input()) == 1:
    #Parte 1
    (N, K) = map(int, input().split())
    semaforos=[]
    for i in range(0, K):
        semaforos.append(int(input()))
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    n=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    for p in primes:
        for j in semaforos:
            while j % (n[p]*p) == 0:
                n[p] = n[p]*p
    lcm=1
    for i in n:
        lcm = lcm*i
    print(lcm)
else:
    #Parte 2
    (N, K) = map(int(), input().split())