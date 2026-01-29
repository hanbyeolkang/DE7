import math

def solution(diffs, times, limit):
    def getTime(diffs, times, limit, level):
        time = 0
        for idx, diff in enumerate(diffs):
            if diff <= level:
                time += times[idx]
            else:
                if idx == 0:
                    time += times[0] * (diff - level) + times[0]
                else:
                    time += (times[idx-1] + times[idx]) * (diff - level) + times[idx]
            
            if limit < time:
                time = -1
                break

        return time
    
    level = max(diffs)
    time = getTime(diffs, times, limit, level)
    fail_level = []
    new_level = level

    while time < limit:
        if len(fail_level) == 0:
            new_level = math.ceil(level/2)
        else:
            new_level = math.ceil((level+max(fail_level))/2)

        if level == new_level:
            break

        new_time = getTime(diffs, times, limit, new_level)

        if new_time != -1 and new_time <= limit:
            level = new_level
            time = new_time
        else:
            fail_level.append(new_level)

    return level


diffs = [1, 5, 3]
times = [2, 4, 7]
limit = 30
print(solution(diffs, times, limit))    # 예상 결과 : 3

# https://school.programmers.co.kr/learn/courses/30/lessons/340212