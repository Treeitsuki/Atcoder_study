H, A = map(int, input().split())

#攻撃回数を管理する変数
cnt = 0

while H > 0:
    H -= A
    cnt += 1

print(cnt)