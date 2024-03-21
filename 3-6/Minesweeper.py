#よく分からなかった
#0: 下、1: 右、2: 上、3: 左、4: 右下、5: 右上、6: 左上、7: 左下
DX = [1, 0, -1, 0, 1, -1, -1, 1]
DY = [0, 1, 0, -1, 1, 1, -1, -1]

#入力
H, W = map(int, input().split())
S = [input() for i in range(H)]

#答えを表す二次元配列を別途用意する（'.' のところは 0 とする）
result = [[0 if v == '.' else '#' for v in row] for row in S]

#各マス（i, j）を順に処理
for i in range(H):
    for j in range(W):
        #空きマス以外はそのままにする
        if S[i][j] != '.':
            continue
        
        #周囲 8 マスの '#' の個数を数える
        for dx, dy in zip(DX, DY):
            #マス（i, j）の周囲のマスを(ni, nj)とする
            ni, nj = i + dx, j + dy
            
            #マス（ni, nj）が盤面外の場合はスキップ
            if ni < 0 or ni >= H or nj < 0 or nj >= W:
                continue
            
            # # であれば1増やす
            if S[ni][nj] == '#':
                result[i][j] += 1
                
#出力形式に合わせて出力
for row in result:
    print(*row, sep=' ')