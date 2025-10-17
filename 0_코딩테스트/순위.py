def solution(n, results):
    # graph[x][y] = True : x 가 y 를 이김
    graph = [[False] * (n+1) for _ in range(n+1)]
    for winner, loser in results:
        graph[winner][loser] = True

    # if [a, b], [b, c] then [a, c]
    # b 가 제일 바깥 for 문에 있어야 graph[a][c] 로 인해 생기는 영향을 다시 체크할 수 있음
    for b in range(1, n+1):
        for a in range(1, n+1):
            for c in range(1, n+1):
                if graph[a][b] and graph[b][c]:
                    graph[a][c] = True

    answer = 0
    for i in range(1, n+1):
        knowCnt = 0     # 확실하게 알 수 있는 결과 수
        for j in range(1, n+1):
            if i == j:
                continue

            # i, j 둘 중에 누가 이겼는지 알면
            if graph[i][j] or graph[j][i]:
                knowCnt += 1
        
        if knowCnt == n-1:
            answer += 1

    return answer


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results)) # 예상 결과 : 2