def solution(bridge_length, weight, truck_weights):
    answer = 0
    cur_weight = 0
    bridge = [ 0 for _ in range(bridge_length)]

    while truck_weights:
        answer += 1
        cur_weight -= bridge.pop(0)     # 다리를 완전히 지남

        if cur_weight + truck_weights[0] <= weight:
            tw = truck_weights.pop(0)
            bridge.append(tw)           # 다리에 새롭게 진입
            cur_weight += tw
        else:
            bridge.append(0)

    # 다리 위에 있는 마지막 트럭이 빠져나올 시간 더해주기
    answer += bridge_length

    return answer


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

print(solution(bridge_length, weight, truck_weights))   # 예상 결과 : 8

# https://school.programmers.co.kr/learn/courses/30/lessons/42583