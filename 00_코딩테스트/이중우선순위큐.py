import heapq

def solution(operations):
    queue = []

    for operation in operations:
        op, num = operation.split(' ')
        num = int(num)

        if op == 'I':
            heapq.heappush(queue, num)
        elif len(queue) > 0:
            if num == 1:
                queue.sort()
                del queue[-1]
            else:
                heapq.heappop(queue)

    if len(queue) == 0:
        return [0, 0]
    elif len(queue) == 1:
        return [queue[0], queue[0]]
    else:
        queue.sort()
        return [queue[-1], queue[0]]



operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))     # 예상 결과 : [333, -45]

# https://school.programmers.co.kr/learn/courses/30/lessons/42628