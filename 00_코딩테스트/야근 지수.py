import heapq

def solution(n, works):
    hq = []
    for w in works:
        heapq.heappush(hq, -w)
    
    for i in range(n):
        val = -heapq.heappop(hq)
        if val == 0:
            break;
        heapq.heappush(hq, -(val-1))
    
    return sum(x*x for x in hq)


works = [1, 1]
n = 3
print(solution(n, works))  # 예상 결과 : 12

# https://school.programmers.co.kr/learn/courses/30/lessons/12927