# in_out_office_total = []
# in_out_office = input("사원들의 출근시간과 퇴근시간을 입력해 주세요. (모두 입력하셨으면 '종료'를 입력해 주세요) : ")
# if in_out_office != "종료":
#     split_in_out = in_out_office.split()


a = []
b = "12:02:45 18:12:30"
d = b.split()
# print(d)



aaa = ["12:02:45 18:12:30", "10:12:45 13:12:30", "09:02:45 19:12:30"]
# print(aaa[0])
# print(type(aaa[0]))
for i in aaa:
    b = i.split()
    in_time = b[0].split(":")
    out_time = b[1].split(":")

    # split_in_time =
    print(in_time)
    print(out_time)