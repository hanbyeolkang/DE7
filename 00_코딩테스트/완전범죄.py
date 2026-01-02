def solution(info, n, m):
    answer = n
    visited = set()

    def dfs(idx, a, b):
        nonlocal answer
        visited.add((idx, a, b))

        if a >= n or b >= m:
            return
        if a >= answer:
            return
        if idx == len(info):
            answer = min(answer, a)
            return
        
        newA = a+info[idx][0]
        newB = b+info[idx][1]
        if (idx+1, newA, b) not in visited:
            dfs(idx+1, newA, b)
        if (idx+1, a, newB) not in visited:
            dfs(idx+1, a, newB)

    dfs(0, 0, 0)
    return answer if answer != n else -1


info = [[1, 2], [2, 3], [2, 1]]
n = 4
m = 4
print(solution(info, n, m)) # 예상 결과 : 2

# https://school.programmers.co.kr/learn/courses/30/lessons/389480