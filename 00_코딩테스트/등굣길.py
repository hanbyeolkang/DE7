def solution(m, n, puddles):
    # 왼쪽에서 오거나, 위에서 내려온 경우만 최단 거리
    load = [[0 for _ in range(m)] for _ in range(n)]
    for x, y in puddles:
        load[y-1][x-1] = -1     # 순서 주의

    load[0][0] = 1
    for i in range(n):
        for j in range(m):
            if load[i][j] == -1:
                load[i][j] = 0
                continue

            if i > 0:
                load[i][j] += load[i-1][j]
            if j > 0:
                load[i][j] += load[i][j-1]

    return load[n-1][m-1] % 1000000007


m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles)) # 예상 결과 : 4

# https://school.programmers.co.kr/learn/courses/30/lessons/42898