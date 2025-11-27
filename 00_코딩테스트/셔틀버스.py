from datetime import datetime, timedelta

def solution(n, t, m, timetable):
    TIME_FORMAT = "%H:%M"

    shuttles = []   # 셔틀 버스 리스트 (출발 시간, 탑승 가능한 수)
    shuttles.append([datetime.strptime("09:00", TIME_FORMAT), m])
    for i in range(1, n):
        shuttles.append([shuttles[0][0] + timedelta(minutes=t*i), m])
    last_shuttle_time = shuttles[-1][0] # 마지막 출발 시간
    
    timetable.sort()
    
    success_time = []   # 탑승에 성공한 리스트
    departure_time, available_cnt = shuttles.pop(0)
    crew = timetable.pop(0)

    while crew:
        crew_time = datetime.strptime(crew, TIME_FORMAT)

        if crew_time <= departure_time and available_cnt > 0:
            # 탑승 가능
            available_cnt -= 1
            success_time.append(crew_time)
            crew = timetable.pop(0) if len(timetable) > 0 else None
        else:
            # 탑승 불가능. 다음 차량이 있다면 대기.
            if len(shuttles) > 0:
                departure_time, available_cnt = shuttles.pop(0)
            else:
                break
    
    if available_cnt > 0 or len(shuttles) > 0:
        # 자리가 남았으면, 마지막 셔틀 시간에 타면됨.
        return last_shuttle_time.strftime(TIME_FORMAT)
    else:    
        # 마지막으로 탑승 성공한 사람보다 1분 먼저 도착해야함.
        last_success_time = success_time[-1] + timedelta(minutes=-1)
        return last_success_time.strftime(TIME_FORMAT)


n, t, m = 1, 1, 5
timetable = ["08:00", "08:01", "08:02", "08:03"]
print(solution(n, t, m, timetable)) # 예상 결과 : "09:00"

# https://school.programmers.co.kr/learn/courses/30/lessons/17678