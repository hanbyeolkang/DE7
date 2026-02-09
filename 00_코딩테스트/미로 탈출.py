from collections import deque

def solution(maps):
    def bfs(maps, start, target):
        n, m = len(maps), len(maps[0])
        visited = [[False]*m for _ in range(n)]

        sx, sy = -1, -1
        for i in range(n):
            for j in range(m):
                if maps[i][j] == start:
                    sx, sy = i, j
                    break
            if sx != -1:
                break
    
        q = deque()
        q.append((sx, sy, 0))
        while q:
            x, y, d = q.popleft()
            if maps[x][y] == target:
                return d

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] != 'X' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny, d+1))
        
        return -1
    

    maps = [list(x) for x in maps]

    distSL = bfs(maps, 'S', 'L')
    if distSL == -1:
        return -1
    distLE = bfs(maps, 'L', 'E')
    if distLE == -1:
        return -1
    
    return distSL + distLE


maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
print(solution(maps))   # 예상 결과 : 16

# https://school.programmers.co.kr/learn/courses/30/lessons/159993