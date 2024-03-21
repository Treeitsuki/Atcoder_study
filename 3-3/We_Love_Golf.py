K = int(input())

A, B = map(int, input().split())

#フラグ：調べた範囲内にKの倍数があったかどうか
exist = False

#A以上、B+1未満の範囲になるから要注意！！
for i in range (A, B + 1):
    if i % K == 0:
        exist = True

print("OK" if exist else "NG")