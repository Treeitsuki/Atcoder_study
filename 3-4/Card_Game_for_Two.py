N = int(input())
a = list(map(int, input().split()))

#配列 a の各要素を大きい順にソートする
#a.sort()   デフォルトでは小さい順にソートする
a.sort(reverse=True)

#答えを表す変数
result = 0

#配列 a の各要素を交互に足し引きしていく
for i in range(N):
    if i % 2 == 0:
        result += a[i]
    else:
        result -= a[i]

print(result)
