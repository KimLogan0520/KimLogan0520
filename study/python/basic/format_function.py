# "{}".format(10)
# "{} {}".format(10, 20)
# string_a = "{}".format(10)
# print(string_a, type(string_a))

# 정수
# output_a = "{:d}".format(52)

# 특정 칸에 출력하기
# output_b = "{:5d}".format(52) # 5칸
# output_c = "{:10d}".format(52) # 10칸

# 빈칸을 0으로 채우기
# output_d = "{:05d}".format(52) # 양수
# output_e = "{:05d}".format(-52) # 음수

# print(output_a)
# print(output_b)
# print(output_c)
# print(output_d)
# print(output_e)

# output_f = "{:+d}".format(52)
# output_g = "{:-d}".format(-52)
# output_h = "{: d}".format(52)
# output_i = "{: d}".format(-52)

# print(output_f)
# print(output_g)
# print(output_h)
# print(output_i)

num = 52.273
output_a = "{:f}".format(num)
output_b = "{:15f}".format(num)
output_c = "{:+15f}".format(num)
output_d = "{:+015f}".format(num)
print(output_a)
print(output_b)
print(output_c)
print(output_d)

output_aa = "{:15.3f}".format(num)
output_bb = "{:15.2f}".format(num)
output_cc = "{:15.1f}".format(num)
print(output_aa)
print(output_bb)
print(output_cc)

# 의미없는 소수점 제거하기
output_x = 52.0
output_y = "{:g}".format(output_x)
print(output_x)
print(output_y)