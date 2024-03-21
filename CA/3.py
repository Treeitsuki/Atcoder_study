N, T = map(int, input().split())

A = []
for _ in range(N):
    A.append(int(input()))

open = 0
i = 0

for i in range(N-1):
    if A[i+1] > A[i] + T:
        open += T
    
    else:
        for j in range(N-i):
            if A[i+j] > A[i+1] + T:
                open += (A[i+1] + T - A[i])
            

print(open)