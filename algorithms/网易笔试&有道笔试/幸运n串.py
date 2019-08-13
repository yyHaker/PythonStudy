
def count(str):
    res = 0
    cnt = 0
    change = 2
    i = 0
    while i < len(str):
        if str[i] == 'N':
            cnt += 1
            i += 1
        elif change:
            change -= 1
            cnt += 1
            i += 1
        else:
            cnt = 0
            change = 2
            # 往回走
            i = i - 1
            c = 1
            while i > 0:
                if str[i] == 'N':
                    i = i - 1
                elif c > 0:
                    i = i - 1
                    c = c - 1
                else:
                    i = i + 1
                    break
        res = max(res, cnt)
    return res

t = int(input().strip())
while t:
    t -= 1
    str = input().strip()
    res = count(str)
    print(res)

"""
3
NNTN
NNNNGGNNNN
NG NNNN GNNNNNNNN SNNNN
"""