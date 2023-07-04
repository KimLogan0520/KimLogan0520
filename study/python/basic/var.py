# py = 3.14159265
# print(py)

# 원의 둘레와 넓이 구하기
pi = 3.14159265
r = 10

print("원주율 :", pi)
print("반지름 :", r)
print("원의 둘레 :", 2 * pi * r)
print("원의 넓이 :", pi * (r ** 2))  # `pi * (r**2)`는 `pi * r * r` 로도 표현 가능

string = input("인사말을 입력해보세요 > ")
print(string)

# 캐스트
string_a = input("입력A > ")
int_a = int(string_a)

string_b = input("입력B > ")
int_b = int(string_b)

print("문자열 자료 :", string_a + string_b)
print("숫자 자료 :", int_a + int_b)