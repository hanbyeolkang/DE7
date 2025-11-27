def solution(sticker):
    if len(sticker) < 4:
        return max(sticker)

    # 마지막 스티커 선택하지 않음
    sticker1 = sticker[:-1]
    dp1 = [0 for _ in sticker1]
    dp1[0], dp1[1] = sticker1[0], sticker1[1]
    dp1[2] = max(sticker1[2] + sticker1[0], sticker1[1])

    # 첫번째 스티커 선택하지 않음
    sticker2 = sticker[1:]
    dp2 = [0 for _ in sticker2]
    dp2[0], dp2[1] = sticker2[0], sticker2[1]
    dp2[2] = max(sticker2[2] + sticker2[0], sticker2[1])

    for i in range(3, len(sticker)-1):
        dp1[i] = max(sticker1[i] + dp1[i-3], sticker1[i] + dp1[i-2], dp1[i-1])
        dp2[i] = max(sticker2[i] + dp2[i-3], sticker2[i] + dp2[i-2], dp2[i-1])
    
    return max(dp1[-1], dp2[-1])


sticker = [4, 3, 2, 9, 4]
print(solution(sticker))    # 예상 결과 : 13

# https://school.programmers.co.kr/learn/courses/30/lessons/12971