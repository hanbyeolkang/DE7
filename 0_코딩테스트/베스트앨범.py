def solution(genres, plays):
    counts = {}                     # key: 장르, value: 총 재생횟수
    for i in range(len(genres)):
        counts[genres[i]] = counts.get(genres[i], 0) + plays[i]
    counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    answer = []
    for i in range(len(counts)):    # 제일 많이 들은 장르부터, 장르의 개수만큼 반복
        idx1, idx2 = -1, -1         # 베스트1, 베스트2 곡의 인덱스
        for idx in range(len(genres)):
            if counts[i][0] == genres[idx]:     # 현재 찾고 있는 장르가 맞으면
                if idx1 == -1:                  # 베스트1, 베스트2 순서대로 일단 채우기
                    idx1 = idx
                elif idx2 == -1:
                    idx2 = idx
                elif plays[idx2] < plays[idx] or (plays[idx2] == plays[idx] and idx < idx2):
                    idx2 = idx

                # 베스트1, 베스트2 비교해서 순서 맞추기
                if plays[idx1] < plays[idx2] or (plays[idx1] == plays[idx2] and idx2 < idx1):
                    idx1, idx2 = idx2, idx1
                
        if idx1 != -1:
            answer.append(idx1)
        if idx2 != -1 and idx1 != idx2:
            answer.append(idx2)

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))  # 예상 결과 : [4, 1, 3, 0]

# https://school.programmers.co.kr/learn/courses/30/lessons/42579