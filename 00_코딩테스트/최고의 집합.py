def solution(n, s):
    answer = [s//n for _ in range(n)]
    if s % n != 0:
        total = sum(answer)
        for i in range(s - total):
            answer[n-1-i] += 1
            
    if answer[0] == 0:
        return [-1]
    return answer


n = 2
s = 9
print(solution(n, s))   # 예상 결과 : [4, 5]

# https://school.programmers.co.kr/learn/courses/30/lessons/12938