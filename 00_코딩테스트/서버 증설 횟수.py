def solution(players, m, k):
    addCnts = [p//m for p in players]    # 각 시간에 필요한 추가 서버수
    
    answer = 0
    for i in range(len(addCnts)):
        addCnt = addCnts[i]
        if addCnt:
            answer += addCnt        # 서버 증설
            for j in range(1, k):   # k 시간 동안 운영
                if i+j < len(addCnts) and addCnts[i+j] != 0:
                    addCnts[i+j] = max(addCnts[i+j]-addCnt, 0)  # 음수가 되는 경우 방지
    
    return answer


players = [0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5]
m = 3
k = 5
print(solution(players, m, k))  # 예상 결과 : 7

# https://school.programmers.co.kr/learn/courses/30/lessons/389479