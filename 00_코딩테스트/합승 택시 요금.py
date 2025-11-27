import heapq

# 무한
INF = float('inf')

# start부터 각 지점(1~n)까지 최소 요금 구하기
def dijkstra(n, graph, start):
    dist = [INF]*(n+1)  # start 에서 각 지점까지의 최소 요금
    hq = [(0, start)]   # (비용, 노드번호) 튜플을 담을 최소 힙 (우선순위 큐. 비용순)

    while hq:
        fare, node = heapq.heappop(hq)

        # 이미 저장되어 있는 최단 요금보다 크면 pass
        if dist[node] < fare:
            continue

        for next in range(1, n+1):
            # newFare = node에서 next까지 가는 요금
            newFare = graph[node][next]
            if newFare == INF:
                continue

            # newFare 에 start에서 node까지 오는데 든 요금 더해주기
            newFare += fare
            if newFare < dist[next]:
                dist[next] = newFare
                if node != next:
                    heapq.heappush(hq, (newFare, next))
    
    return dist


def solution(n, s, a, b, fares):
    graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        graph[i][i] = 0

    for fare in fares:
        x, y, f = fare[0], fare[1], fare[2]
        graph[x][y] = f
        graph[y][x] = f

    sFares = dijkstra(n, graph, s)  # s에서 1~n까지 최소 요금 리스트
    aFares = dijkstra(n, graph, a)  # a에서 1~n까지 최소 요금 리스트
    bFares = dijkstra(n, graph, b)  # b에서 1~n까지 최소 요금 리스트

    answer = INF
    for i in range(1, n+1):
        fare = sFares[i] + aFares[i] + bFares[i]
        answer = min(answer, fare)

    return answer


n, s, a, b = 6, 4, 6, 2
fares = [
    [4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24],
    [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]
]

print(solution(n, s, a, b, fares))  # 예상 결과 : 82

# https://school.programmers.co.kr/learn/courses/30/lessons/72413