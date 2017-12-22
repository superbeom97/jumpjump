# 그 시간 사무실에 몇 명이 있었나?
#
# A 사무실에는 특정일자의 출퇴근 시간이 기록된 거대한 로그파일이 있다고 한다.
#
# 파일의 형식은 다음과 같다. (한 라인에서 앞부분은 출근시간(HH:MM:SS), 뒷부분은 퇴근시간이다)
#
# 09:12:23 11:14:35
# 10:34:01 13:23:40
# 10:34:31 11:20:10
#
# 특정시간을 입력(예:11:05:20)으로 주었을 때 그 시간에 총 몇 명이 사무실에 있었는지 알려주는 함수를 작성하시오.


# HH = 00 - 23, MM = 00 - 59, SS = 00 - 59
def Check_people():
    in_out_office_total = []
    print("<< 사원들의 출근시간과 퇴근시간을 입력해 주세요. (모두 입력하셨으면 '종료'를 입력해 주세요) >>")
    while True:
        in_out_office = input()
        if in_out_office != "종료":
            in_out_office_total.append(in_out_office)
        else:
            break

    search_time = input("알아보고 싶은 시간을 입력하시오: ") # search_time이 출근시간보다 크고 퇴근시간보다 작으면 돼
    div_search_time = search_time.split(":")
    count = 0

    for i in in_out_office_total:
        in_out_time = i.split()
        in_time = in_out_time[0].split(":")
        out_time = in_out_time[1].split(":")

        if in_time[0] < div_search_time[0]:
            count += 1
        elif in_time[0] == div_search_time[0]:
            if in_time[1] < div_search_time[1]:
                count += 1
            elif in_time[1] == div_search_time[1]:
                if in_time[2] <= div_search_time[2]:
                    count += 1

        if out_time[0] < div_search_time[0]:
            count -= 1
        elif out_time[0] == div_search_time[0]:
            if out_time[1] < div_search_time[1]:
                count -= 1
            elif out_time[1] == div_search_time[1]:
                if out_time[2] < div_search_time[2]:
                    count -= 1

    print("'%s'에 사무실에는 %s명의 인원이 있었습니다." % (search_time, count))


while True:
    Check_people()