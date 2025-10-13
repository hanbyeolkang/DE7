def solution(n):
    # if n == 1:
    #     return [1]
    
    answer = []
    for i in range(1, n+1):
        arr = [0]*i
        answer.append(arr)

    '''
        n번 아래로
        n-1번 오른쪽으로
        n-2번 대각선으로
        ...
        1번  ...
    '''
    i, j, num = -1, 0, 0
    arrow = 0   # 0: 아래, 1: 오른쪽, 2: 왼쪽위

    for x in range(0, n):
        for y in range(n, 0, -1):
            num += 1
            if arrow == 0:
                i += 1
            elif arrow == 1:
                j += 1
            else:
                i -= 1
                j -= 1
            answer[i][j] = num
        n -= 1
        arrow = (arrow + 1) % 3

    return sum(answer, [])  # 1차원 배열로


print(solution(4))

# https://school.programmers.co.kr/learn/courses/30/lessons/68645