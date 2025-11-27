def solution(n):
    answer = []
    for i in range(1, n+1):
        arr = [0]*i
        answer.append(arr)

    i, j, num, nn = -1, 0, 0, n
    arrow = 0   # 0: 아래, 1: 오른쪽, 2: 왼쪽위
    
    for x in range(0, n):           # 0 부터 n 까지 반복
        for y in range(nn, 0, -1):  # n번, n-1번, n-2번 .. 1번
            num += 1
            if arrow == 0:
                i += 1
            elif arrow == 1:
                j += 1
            else:
                i -= 1
                j -= 1
            answer[i][j] = num
        nn -= 1
        arrow = (arrow + 1) % 3

    return sum(answer, [])  # 1차원 배열로


print(solution(4))  # 예상 결과 : [1, 2, 9, 3, 10, 8, 4, 5, 6, 7]

# https://school.programmers.co.kr/learn/courses/30/lessons/68645