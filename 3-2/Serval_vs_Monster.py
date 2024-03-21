H, A = map(int, input().split())

#「/」だと浮動小数点になる（例：3 / 2 = 1.5）
#「//」だと商のみを求められる
if H % A ==0:
    print(H // A)
else:
    print(H // A +1)