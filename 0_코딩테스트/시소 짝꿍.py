from collections import Counter

def solution(weights):
    answer = 0
    weights.sort()
    counter = Counter(weights)
    for (w, c) in counter.items():
        answer += c * (c-1) // 2        # 1:1
        answer += c * counter[w*2]      # 2:1
        answer += c * counter[w*3/2]    # 3:2
        answer += c * counter[w*4/3]    # 4:3
    return answer


weights = [100, 180, 360, 100, 270]     # answer = 4
#weights = [200, 100, 100, 200, 100]    # answer = 10
print(solution(weights))

# https://school.programmers.co.kr/learn/courses/30/lessons/152996