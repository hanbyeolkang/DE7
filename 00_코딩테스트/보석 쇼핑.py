def solution(gems):
    answer = [0, len(gems)-1]
    curr = [0, 0]

    s = set(gems)
    dict = {}
    
    for i, gem in enumerate(gems):
        # i번째 보석 추가
        curr[1] = i
        dict[gem] = dict.get(gem, 0) + 1

        # 현재 구간의 제일 왼쪽부터 제거할 수 있는 보석 제거
        for j in range(curr[0], i):
            first_gem = gems[j]
            if dict.get(first_gem, 0) > 1:
                dict[first_gem] -= 1
                curr[0] = j+1
            else:
                break

        if len(s) == len(dict) and curr[1]-curr[0] < answer[1]-answer[0]:
            answer = [curr[0], curr[1]]

    return [answer[0]+1, answer[1]+1]


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))   # 예상 결과 : [3, 7]

# https://school.programmers.co.kr/learn/courses/30/lessons/67258