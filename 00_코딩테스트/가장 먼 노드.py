import heapq

def dijkstra(n, nodes, start_node):
    INF = float('inf')
    dist = [INF for _ in range(n+1)]
    dist[start_node] = 0

    hq = [(0, start_node)]              # (거리, 노드). 거리 짧은 순서대로 정렬
    while hq:
        cur_dist, cur_node = heapq.heappop(hq)

        if dist[cur_node] < cur_dist:   # 이미 저장된 거리가 더 짧으면 continue
            continue

        for next_node in nodes[cur_node]:
            if cur_dist + 1 < dist[next_node]:  # 지금 있는 노드를 거쳐서 가는게, 기존 거리보다 짧아지면
                heapq.heappush(hq, (cur_dist + 1, next_node))
                dist[next_node] = cur_dist + 1

    return dist


def solution(n, edge):
    nodes = [set() for _ in range(n+1)] # nodes[i] : i번 노드와 연결된 노드들
    for a, b in edge:
        nodes[a].add(b)
        nodes[b].add(a)
    
    dist = dijkstra(n, nodes, 1)        # dist[i] : 1번 노드부터 i번 노드까지의 거리
    return dist.count(max(dist[1:]))    # dist[0] = INF 주의


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))  # 예상 결과 : 3

# https://school.programmers.co.kr/learn/courses/30/lessons/49189