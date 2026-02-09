def solution(targets):
    targets.sort(key=lambda x:-x[1])

    answer = 0
    point = 0.0
    while(targets):
        s, e = targets.pop()
        if s < point and point < e:
            continue
        else:
            answer += 1
            point = e - 0.5     # 실수 좌표에서 발사 가능

    return answer


targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
print(solution(targets))    # 예상 결과 : 3

# https://school.programmers.co.kr/learn/courses/30/lessons/181188