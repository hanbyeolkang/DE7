import math

def solution(n, stations, w):
    answer = 0
    position = 1
    
    # 각 기지국의 왼쪽 구간 확인
    for s in stations:
        if position < s-w:
            answer += math.ceil((s-w-position)/(2*w + 1))   # 올림
        position = s+w+1
        
    # 마지막 기지국의 오른쪽 구간 확인
    if position <= n:
        answer += math.ceil((n-position+1)/(2*w + 1))       # 올림
        
    return answer


n = 11
stations = [4, 11]
w = 1
print(solution(n, stations, w)) # 예상 결과 : 3

# https://school.programmers.co.kr/learn/courses/30/lessons/12979