import itertools

def solution(n, q, ans):
    arr = [x for x in range(1, n+1)]            # 1 부터 n 까지의 정수가 담긴 리스트
    nCr = list(itertools.combinations(arr, 5))  # 리스트에서 5개씩 뽑은 조합
    
    answer = 0
    for i in range(len(nCr)):
        isCorrect = False
        for j in range(len(q)):
            # 조합과 j+1 번째 시도의 교집합의 개수
            if len(list(set(nCr[i]).intersection(q[j]))) != ans[j]:
                break
        else:
            isCorrect = True
            
        if isCorrect:
            answer += 1
    
    return answer


n = 10
q = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]]
ans = [2, 3, 4, 3, 3]
print(solution(n, q, ans))  # 예상 결과 : 3

# https://school.programmers.co.kr/learn/courses/30/lessons/388352