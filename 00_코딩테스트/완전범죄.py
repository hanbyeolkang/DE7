def solution(info, n, m):
    # b/a asc, b desc
    info.sort(key=lambda x: (x[1]/x[0], -x[1]))
    
    sumA, sumB = 0, 0
    for i in info:
        if sumB + i[1] < m:
            sumB += i[1]
        else:
            sumA += i[0]
    
    if sumA < n:
        return sumA
    else:
        return -1


info = [[1, 2], [2, 3], [2, 1]]
n = 4
m = 4
print(solution(info, n, m)) # 예상 결과 : 2

# https://school.programmers.co.kr/learn/courses/30/lessons/389480