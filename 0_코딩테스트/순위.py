from collections import defaultdict


def topologicalSort(n, results):
    graph = defaultdict(list)
    indegree = [0] * (n + 1)        # 진입차수
    nodes = set(range(1, n + 1))    # 전체 노드. 1부터 n까지

    for winner, loser in results:
        graph[winner].append(loser)
        indegree[loser] += 1        # 내 앞에 진입차수 만큼 있어야 함.

    orders = []

    def dfs(path, indeg):
        if len(path) == len(nodes): # 모두 방문했으면 경로 저장
            orders.append(path[:])  # path 깊은 복사
            return
        
        for node in sorted(nodes):
            # 내 앞에 있어야 하는게 없고, 아직 방문 전이면
            if indeg[node] == 0 and node not in path:
                new_indeg = indeg[:]
                new_indeg[node] = -1        # 방문 처리
                for nxt in graph[node]:     # 내 뒤에 오는 노드들
                    new_indeg[nxt] -= 1     # 진입차수 -1 시켜줌
                dfs(path + [node], new_indeg)

    dfs([], indegree[:])
    return orders


def findFixedOrder(n, orders):
    fixed = []
    for i in range(n):
        # 가능한 모든 경로에서 순서가 같으면
        same = all(order[i] == orders[0][i] for order in orders)
        if same:
            fixed.append(orders[0][i])

    return fixed


def solution(n, results):
    orders = topologicalSort(n, results)    # 가능한 모든 순서. 위상 정렬.
    fixed = findFixedOrder(n, orders)       # 모든 순서에서 고정된 순서인 노드들.
    return len(fixed)


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results)) # 예상 결과 : 2