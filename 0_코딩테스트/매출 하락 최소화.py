def solution(sales, links):
    sales = [0] + sales                     # idx 시작을 1로 맞춰줌
    link = [[] for _ in range(len(sales))]  # link[i]: i번 노드의 자식 노드들
    dp = [[0, 0] for _ in range(len(sales))]    # dp[i][0]: 본인 참석 O, dp[i][1]: 본인 참석 X

    for parent, child in links:
        link[parent].append(child)
        

    # 노드 순회하면서 dp 값 구하기
    def solve(i):
        # 리프 노드이면
        if len(link[i]) == 0:
            dp[i][0] = sales[i]
            dp[i][1] = 0
            return
        
        for child in link[i]:
            solve(child)

        dp[i][0] = sales[i] + sum(min(dp[k][0], dp[k][1]) for k in link[i])
        dp[i][1] = findMinSumWithAtLeastOneAttend(link[i])
        
        
    # 자식 노드 중 최소 하나라도 참석할 때의 최소 매출 찾기
    def findMinSumWithAtLeastOneAttend(nodes):
        total = 0
        allNoAttend = True
        minDiff = float('inf')

        for child in nodes:
            attend, noAttend = dp[child][0], dp[child][1]
            if attend <= noAttend:  # 참석함
                total += attend
                allNoAttend = False
            else:                   # 참석안함
                total += noAttend
                minDiff = min(minDiff, attend - noAttend)   # 가장 적은 매출 차이

        if allNoAttend:         # 모두 참석 안하면
            total += minDiff    # 제일 차이가 적은 노드가 참석해야함

        return total
    

    solve(1)
    return min(dp[1][0], dp[1][1])


sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
print(solution(sales, links))   # 예상 결과 : 2