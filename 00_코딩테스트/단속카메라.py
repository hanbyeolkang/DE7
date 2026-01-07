def solution(routes):
    # 나간 지점으로 정렬
    routes.sort(key=lambda x: x[1])

    answer = 1
    position = routes[0][1]
    for r in routes[1:]:
        # 이후 진입이면 그 차량이 나가는 지점에 카메라 설치
        if position < r[0]:
            position = r[1]
            answer += 1

    return answer


routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes)) # 예상 결과 : 2

# https://school.programmers.co.kr/learn/courses/30/lessons/42884