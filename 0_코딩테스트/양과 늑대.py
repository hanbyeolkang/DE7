def solution(info, edges):
    info = [1 if x == 0 else -1 for x in info]  # 1: 양, -1: 늑대
    graph = [set() for _ in range(len(info))]   # i번 노드에서 갈 수 있는 노드들
    for [p, c] in edges:
        graph[p].add(c)

    def visit(node, info, graph, sumCnt, sheepCnt, nextNodes):
        if sumCnt + info[node] == 0:    # 양, 늑대 수가 같으면 방문 종료
            return
        
        sumCnt += info[node]
        if info[node] == 1:
            sheepCnt += 1
            nonlocal maxSheepCnt
            maxSheepCnt = max(sheepCnt, maxSheepCnt)    # 최대 양의 수 갱신

        nextNodes.discard(node)         # 방문할 노드 리스트에서 현재 노드 제거
        nextNodes.update(graph[node])   # 방문할 노드 리스트에 갈 수 있는 자식 노드 추가

        for next in nextNodes:
            visit(next, info, graph, sumCnt, sheepCnt, nextNodes.copy())    # copy 주의
    
    maxSheepCnt = 0
    visit(0, info, graph, 0, 0, set())
    return maxSheepCnt


info = [0,0,1,1,1,0,1,0,1,0,1,1]                        # info[i] : i번 노드에 있는 양(0) 또는 늑대(1)
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]   # [부모, 자식]

print(f'- answer = {solution(info, edges)}')    # 예상 결과 : 5

# https://school.programmers.co.kr/learn/courses/30/lessons/92343