def solution(n, computers):
    # i 노드와 i 노드에서 갈 수 있는 모든 노드 방문
    def visit(i, computers):
        nonlocal visit_list
        visit_list[i] = True
        for j, connect in enumerate(computers[i]):
            if i != j and connect == 1 and visit_list[j] is False:
                visit(j, computers)

    answer = 0
    visit_list = [False for _ in range(n)]
    for i in range(n):
        if visit_list[i] is False:
            visit(i, computers)
            answer += 1

    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))   # 예상 결과 : 2

# https://school.programmers.co.kr/learn/courses/30/lessons/43162