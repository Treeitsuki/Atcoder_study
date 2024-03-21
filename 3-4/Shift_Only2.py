#整数 num が 2 で何回割れるか
def how_many_times(num):
    #2 で割り切れる回数を表す変数
    cnt = 0
    
    #2 で割れる限り、割り続ける
    while num % 2 == 0:
        num //= 2
        
        cnt += 1
    
    return cnt

#十分に大きい値
INF = 2 ** 30   #2^30とこと

#入力
N = int(input())
A = list (map(int, input().split()))

#答えを表す変数（十分に大きい値に初期化しておく）
#一般になんらかの最小値を求める問題では、最小値を表す変数を「十分に大きい値」で初期化しておくと便利
result = INF

for a in A:
    #2 で割れる回数の最小値を求める
    cnt = how_many_times(a)
    
    #result より cnt の方が小さい場合は更新する
    result = min(result, cnt)
    
#出力
print(result)