def solution(mats, park):
    def chkPark(i, j, m):
        if len(park) < i+m or len(park[0]) < j+m:
            return False
        
        return all(park[a][b] == '-1' for a in range(i, i+m) for b in range(j, j+m))
        
    
    mats.sort(reverse=True)     # 큰 돗자리부터 검사

    for m in mats:
        for i in range(len(park)-m+1):
            for j in range(len(park[0])-m+1):
                if chkPark(i, j, m):
                    return m
    
    return -1


mats = [2,3,5]
park = [["A", "A", "-1", "B", "B", "B", "B", "-1"],
        ["A", "A", "-1", "B", "B", "B", "B", "-1"],
        ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
        ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"],
        ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"],
        ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"]]

print(solution(mats, park)) # 예상 결과 : 3

# https://school.programmers.co.kr/learn/courses/30/lessons/340198