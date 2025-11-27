from datetime import datetime, timedelta

def solution(lines):
    start_times = []
    end_times = []

    for line in lines:
        arr = line.split()

        end_time = datetime.strptime(" ".join(arr[:2]), "%Y-%m-%d %H:%M:%S.%f")
        duration = float(arr[2][:-1])   # 's' 제거

        start_time = end_time - timedelta(seconds=duration) + timedelta(milliseconds=1)
        start_times.append(start_time)
        end_times.append(end_time)

    max_cnt = 0
    for i in range(len(end_times)):
        cnt = 0
        cur_time = end_times[i]

        # i 와 i 보다 늦게 끝나는 트래픽만 확인하면 됨
        for j in range(i, len(start_times)):
            # 내가 끝나고 1초 되기 전에 실행되면 카운트
            # 어차피 나보다 늦게 끝나므로 end_time 은 볼 필요 없음 (문제 정렬 조건)
            if start_times[j] < cur_time + timedelta(seconds=1):
                cnt += 1
        max_cnt = max(max_cnt, cnt)

    return max_cnt


lines = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
print(solution(lines))  # 예상 결과 : 1

# https://school.programmers.co.kr/learn/courses/30/lessons/17676