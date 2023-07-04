# x = 25
# print(10 < x < 30)

# not 연산자, and 연산자, or 연산자
# true = True
# print(not true)
# print(!true) ==> js처럼 사용할 순 없음.

# if 조건문
# num = int(input("정수를 입력해주세요. > "))
# if num > 0 :
#     print(f'{num}은 양수입니다.')

# import datetime
# now = datetime.datetime.now()
# time_data = [now.year, now.month, now.day, now.hour, now.minute, now.second]
# print("{}년 {}월 {}일 {}시 {}분 {}초".format(*time_data))
# print(f"{time_data[0]}년 {time_data[1]}월 {time_data[2]}일 {time_data[3]}시 {time_data[4]}분 {time_data[5]}초")

input_num = int(input("정수를 입력해주세요 > "))
if input_num > 0 :
    print(f"입력하신 {input_num}은 양수입니다.")
elif input_num < 0 :
    print(f"입력하신 {input_num}은 음수입니다.")
else :
    print(f"{input_num}을 입력하셨군요.")

if input_num > 0 :
    # TODO xxx...
    # pass
    raise NotImplementedError
else :
    # TODO yyy...
    raise NotImplementedError
