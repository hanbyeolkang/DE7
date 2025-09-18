from functools import cmp_to_key

def solution(numbers):
    strNums = map(str, numbers)
    strNums = sorted(strNums, key=cmp_to_key(compare))
    return ''.join(strNums) if strNums[0] != '0' else '0'


def compare(strNum1, strNum2):
    num1 = strNum1 + strNum2
    num2 = strNum2 + strNum1
    if num1 < num2:
        return 1
    elif num2 < num1:
        return -1
    else:
        return 0


numbers = [6, 10, 2]
answer = solution(numbers)
print(answer)

# 프로그래머스 - 가장 큰 수
# https://school.programmers.co.kr/learn/courses/30/lessons/42746