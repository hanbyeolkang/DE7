import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            break
        elif len(scoville) == 0:
            answer = -1
            break
        
        min2 = heapq.heappop(scoville)
        new_scoville = min1 + 2*min2
        heapq.heappush(scoville, new_scoville)
        answer += 1
        
    return answer


scoville = [1, 2, 3, 9, 10, 12]
K = 7
answer = solution(scoville, K)
print(answer)

# 프로그래머스 - 더 맵게
# https://school.programmers.co.kr/learn/courses/30/lessons/42626