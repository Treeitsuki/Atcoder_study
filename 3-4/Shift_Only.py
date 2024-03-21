N = int(input())
A = list(map(int, input().split()))

#操作回数
cnt = 0

#操作が行えなくなるまで操作を行う
#（判定→操作）→（判定→操作）・・・→終了
while True:
    #操作が行えるかを判定する
    can_do = True
    for i in range(N):
        if A[i] % 2 == 1:
            can_do = False
    
    #操作を行えないならば、反復を打ち切る
    if not can_do:
        break
    
    #操作を行えるならば、操作を行う
    for i in range(N):
        A[i] //= 2  #A[i]にA[i]を2で割った商を代入
    
    #操作回数を1増やす
    cnt += 1
    
print(cnt)