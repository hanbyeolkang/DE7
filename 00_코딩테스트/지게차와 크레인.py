dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

# 외부 연결 확인. 너비 우선 탐색 bfs
def isOutside(storage, x, y):
    outside = False
    
    for k in range(4):  # 상하좌우 확인
        nx, ny = x + dx[k], y + dy[k]
        if storage[nx][ny] == '0':
            storage[x][y] = '0'     # 주변에 0 이 있으면 외부와 연결시켜줌
            outside = True
            break

    if outside:
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if storage[nx][ny] == '1':      # 상하좌우에 크레인으로 꺼낸 자리가 있으면
                storage[nx][ny] = '0'       # 외부와 연결시켜줌
                isOutside(storage, nx, ny)  # 더이상 연결되지 않을때까지 반복해서 찾음


# 지게차 (외부에서 접근 가능한 것만 꺼냄)
def fork(storage, r):
    idxList = []
    for i in range(1, len(storage)-1):
        for j in range(1, len(storage[0])-1):
            if storage[i][j] == r:
                for k in range(4):  # 상하좌우 외부 확인
                    nx, ny = i + dx[k], j + dy[k]
                    if storage[nx][ny] == '0':
                        idxList.append((i, j))
                        break

    # 지워야할 인덱스들 처리
    for i, j in idxList:
        storage[i][j] = '0'         # 0: 외부와 연결
        isOutside(storage, i, j)    # 외부 연결 확인. 크레인으로 꺼낸 자리가 외부랑 연결되면 여기에서 0 으로 바뀜.


# 크레인 (모두 꺼냄)
def crane(storage, r):
    for i in range(1, len(storage)-1):
        for j in range(1, len(storage[0])-1):
            if storage[i][j] == r:
                storage[i][j] = '1'         # 1: 크레인으로 꺼낸 자리
                isOutside(storage, i, j)    # 외부 연결 확인. 크레인으로 꺼낸 자리가 외부로 연결되면 여기에서 0 으로 바뀜.


def solution(storage, requests):
    # 가로+2/세로+2 크기로 2차원 배열 준비. 외부 테두리에 0 추가.
    storage = [list('0' + str + '0') for str in storage]
    storage.insert(0, list('0' * len(storage[0])))
    storage.append(list('0' * len(storage[0])))

    for r in requests:
        if len(r) == 1:
            fork(storage, r)        # 지게차 (외부에서 접근 가능한 것만 꺼냄)
        else:
            crane(storage, r[0])    # 크레인 (모두 꺼냄)


    answer = 0
    for i in range(1, len(storage)-1):
        for j in range(1, len(storage[0])-1):
            if storage[i][j] not in ['0', '1']:
                answer += 1

    return answer
    

storage = ["AZWQY", "CAABX", "BBDDA", "ACACA"]
requests = ["A", "BB", "A"]
print(solution(storage, requests))  # 예상 결과 : 11

# https://school.programmers.co.kr/learn/courses/30/lessons/388353