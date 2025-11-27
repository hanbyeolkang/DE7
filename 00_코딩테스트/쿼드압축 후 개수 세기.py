import numpy as np

def solution(arr):
    answer = [0, 0]

    sum = np.sum(np.array(arr))
    if sum == 0:
        return [1, 0]
    elif sum == len(arr) * len(arr):
        return [0, 1]

    stack = []
    stack.append(arr)
    while stack:
        arr = stack.pop()
        n = len(arr) // 2
        if n == 0:
            if arr[0] == 0:
                answer[0] += 1
            else:
                answer[1] += 1
            continue

        top = arr[:n]
        bottom = arr[n:]
        arrs = []
        arrs.append([row[:n] for row in top])
        arrs.append([row[n:] for row in top])
        arrs.append([row[:n] for row in bottom])
        arrs.append([row[n:] for row in bottom])

        for i in range(4):
            sum = np.sum(np.array(arrs[i]))
            if sum == 0:
                answer[0] += 1
            elif sum == n * n:
                answer[1] += 1
            else:
                stack.append(arrs[i])

    return answer


arr = [
    [1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1],
    [0,0,0,0,1,1,1,1],
    [0,1,0,0,1,1,1,1],
    [0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,1,0,0,1],
    [0,0,0,0,1,1,1,1]
]
print(solution(arr))    # 예상 결과 : [10,15]