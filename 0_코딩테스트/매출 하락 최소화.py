import heapq

def solution(sales, links):
    sales = [-1] + sales                    # sales[i]: i번 직원의 매출
    teams = ['' for _ in range(len(sales))] # teams[i]: i번 직원이 속한 팀들. ','로 이어진 string
    teamInfo = {}                           # key: 팀장, value: (매출, 팀원). 매출 순으로 오름차순

    for leader, staff in links:
        teams[staff] = str(leader)
        if leader not in teamInfo:
            teamInfo[leader] = []
        heapq.heappush(teamInfo[leader], (sales[staff], staff))

    for leader in teamInfo:
        teams[leader] += f',{leader}'   # 팀장이면, 속한 팀에 자신의 팀 추가
    teams[1] = '1'


    def selectEmployee(tCnt, tIdx, visitTeams, sumSales, isLeader):
        teamLeader = list(teamInfo.keys())[tIdx]
        employee = teamLeader if isLeader else teamInfo[teamLeader][0][1]   # 팀장 또는 매출 제일 작은 직원
        eTeams = teams[employee].split(',') # employee가 속한 팀들

        if set(eTeams) - visitTeams:        # 속한 팀 중 방문하지 않은 팀이 있다면
            sumSales += sales[employee]
            visitTeams.update(eTeams)

        nonlocal minSales
        if len(list(teamInfo.keys())) == len(visitTeams):
            minSales = min(minSales, sumSales)
            return

        if tIdx < tCnt-1:
            selectEmployee(tCnt, tIdx+1, visitTeams.copy(), sumSales, True)
            selectEmployee(tCnt, tIdx+1, visitTeams.copy(), sumSales, False)


    minSales = float('inf')
    selectEmployee(len(teamInfo), 0, set(), 0, True)
    selectEmployee(len(teamInfo), 0, set(), 0, False)
    return minSales


sales = [10, 10, 1, 1]
links = [[3,2], [4,3], [1,4]]
print(solution(sales, links))   # 예상 결과 : 2