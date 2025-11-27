def solution(n, money):
    money.sort()
    dp = [0 for _ in range(n+1)]    # dp[n]: n원을 만들 수 있는 경우의 수

    '''
        m = 1
        dp[1] = dp[1]+1 = 0+1 = 1
            dp[2] = dp[2]+dp[1] = 0+1 = 1
            dp[3] = dp[3]+dp[2] = 0+1 = 1
            dp[4] = dp[4]+dp[3] = 0+1 = 1
            dp[5] = dp[5]+dp[4] = 0+1 = 1
        m = 2
        dp[2] = dp[2]+1 = 1+1 = 2
            dp[3] = dp[3]+dp[1] = 1+1 = 2
            dp[4] = dp[4]+dp[2] = 1+2 = 3
            dp[5] = dp[5]+dp[3] = 1+2 = 3
        m = 5
        dp[5] = dp[5]+1 = 3+1 = 4
    '''

    for m in money:                 # 1, 2, 5
        if m > n:
            break;
        dp[m] += 1  # 한개로만 만드는 경우. ex 1원 짜리로 1원. 2원 짜리로 2원. 5원 짜리로 5원 만드는 경우 1가지씩.

        for i in range(m+1, n+1):   # m+1 .. n
            dp[i] += dp[i-m]        # i-m 만드는 각각의 경우에 m원 추가하는 경우 더해줌
            dp[i] %= 1000000007

    return dp[n]


n = 5
money = [1, 2, 5]
print(solution(n, money))   # 예상 결과 : 4

# https://school.programmers.co.kr/learn/courses/30/lessons/12907