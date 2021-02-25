N, Q = input().split()
valores = list( map(int, input().split()[:int(Q)] ) )

calc = 0
aux = 0
N = int(N)
for i in valores: 
    if i == N:
        aux += 1
    else:
        if calc < N and i <= N: 
            calc += i

        if calc == N:
            aux += 1
   
if aux > 0:
    print("SIM")
else:
    print("NAO")
