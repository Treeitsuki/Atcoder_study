#整数 num が 2 で何回割れるか

#map関数は、配列の全要素にアクセスして、関数を適応させることが可能
#繰り返し処理をしなくても全要素にアクセスが可能に！


def how_many_times(num):
    #2 で割り切れる回数を表す変数
    cnt = 0
    
    #2 で割れる限り、割り続ける
    while num % 2 == 0:
        num //= 2
        
        cnt += 1
    
    return cnt

#入力
N = int(input())
A = list(map(int, input().split()))

#A の各要素に how_many_times を適用して、最小値をとる
result = min(map(how_many_times, A))

#出力
print(result)
