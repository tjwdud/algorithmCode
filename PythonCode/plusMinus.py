
def solution(absolutes, signs):
    sum = 0
    print(signs)
    for i in list(zip(absolutes,signs)):
        mark = 1 if i[1] else -1
        sum += i[0]*mark
    return sum
