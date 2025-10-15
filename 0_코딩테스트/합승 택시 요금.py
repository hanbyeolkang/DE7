import copy
import sys
import difflib

# c:현재위치, t:목적지, fList:요금 리스트, vList:방문중인 지점 리스트, rList:가능한 경로 리스트
def bfs(c, t, routes, vList, rList):
    vList.append(c)     # 현재 지점을 방문중인 지점에 넣기
    if c == t:          # 목적지에 도착했으면 가능한 경로 리스트에 추가
        rList.append(copy.deepcopy(vList))
    else:
        # 현재 있는 곳에서 갈 수 있는 지점들 모두 순회
        nList = [y for x, y in routes if x == c and y not in vList]  
        for n in nList:
            bfs(n, t, routes, vList, rList)
            vList.pop()     # 방문 종료


# 경로 요금 계산
def calFare(route, fDict):
    if len(route) == 0:
        return 0
    
    fare = 0
    for i in range(0, len(route)-1):
        x = route[i]
        y = route[i+1]
        fare += fDict[(x, y)]
    return fare


def solution(n, s, a, b, fares):
    # 양방향 간선으로 저장 [x, y], [y, x]
    routes = [[a, b] for x, y, f in fares for a, b in ((x, y), (y, x))]
    aRoutes, bRoutes = [], []
    bfs(s, a, routes, [], aRoutes)  # aRoutes: a 로 가는 모든 경로
    bfs(s, b, routes, [], bRoutes)  # bRoutes: b 로 가는 모든 경로

    # key: (지점1, 지점2), value: 지점1에서 지점2까지의 요금
    fDict = {(a, b): f for x, y, f in fares for a, b in ((x, y), (y, x))}
    smallFare = sys.maxsize
    for ar in aRoutes:
        for br in bRoutes:
            fare = calFare(ar, fDict) + calFare(br, fDict)
            matcher = difflib.SequenceMatcher(None, ar, br)
            match = matcher.find_longest_match(0, len(ar), 0, len(br))
            if match.size > 0:
                abr = ar[match.a : match.a + match.size]    # 겹치는 구간
                fare -= calFare(abr, fDict)

            smallFare = min(smallFare, fare)

    return smallFare


n, s, a, b = 6, 4, 6, 2
fares = [
    [4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24],
    [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]
]

print(solution(n, s, a, b, fares))  # 예상 결과 : 82

# https://school.programmers.co.kr/learn/courses/30/lessons/72413