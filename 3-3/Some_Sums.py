#整数nの各桁の和を求める関数
def calc_sum_digits(n):
    sum_digit = 0   #digit：桁
    
    while n > 0:
        sum_digit += n % 10
        n //= 10    #nを10で割ったときの商が代入される
    
    return sum_digit

#入力
N, A, B = map(int, input().split())

#答えを格納する変数
result = 0

#1以上N以下の整数iを調べていく
for i in range(1, N+1):
    #各桁の和がA以上B以下である場合は加算する
    if A <= calc_sum_digits(i) <= B:
        result += i

print(result)