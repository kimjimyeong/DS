hl = list(map(int, input().split()))
hr = list(map(int, input().split()))

del hl[-1]
del hr[-1]

hLen = len(hl)
vLen = 0
flag = False

for i in range(hLen):
    if hl[i] == -1:
        vLen = hr[i]
        flag = True
        break
    if hr[i] == -1:
        vLen = hl[i]
        flag = True
        break

if flag == True:
    vt = [0 for _ in range(vLen)]
    vb = [0 for _ in range(vLen)]
    check = [[0] * vLen for _ in range(hLen)]
    for i in range(hLen):
        if hr[i] == -1:
            for j in range(hl[i]):
                check[i][j] = 1
        elif hl[i] == -1:
            for j in range(hr[i]):
                check[i][j] = 1
        else:
            for j1 in range(hl[i]):
                check[i][j1] = 1
            for j2 in range(vLen-1, vLen-hr[i]-1, -1):
                check[i][j2] = 1
    v_check = list(zip(*check))

    for i in range(len(v_check)):
        Sum1 = 0
        Sum2 = 0
        for j in range(len(v_check[i])):
            if v_check[i][j] == 0:
                vt[i] = Sum1
                break
            Sum1 += 1
            vt[i] = Sum1
        for j in reversed(range(len(v_check[i]))):
            if v_check[i][j] == 0:
                vb[i] = Sum2
                break
            Sum2 += 1
            vb[i] = -1
    vt.append(-9)
    vb.append(-9)
    print(*vt)
    print(*vb)



