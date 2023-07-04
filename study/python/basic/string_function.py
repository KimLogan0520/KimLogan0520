# 대소문자 바꾸기
lower_string = "abcd"
print(lower_string.upper())
upper_string = "ABCD"
print(upper_string.lower())

input_string = """
    안녕하세요.
문자열의 함수를 알아봅시다.
"""
print(input_string)
print(input_string.strip()) # 왼쪽의 공백만 지울때 : lstrip(), 오른쪽의 공백만 지울때 : rstrip()
# 실제로는 strip()만 많이 쓰고 lstrip(), rstrip()는 많이 사용하지 않는다고함

# find() & rfind()
string = "안녕안녕하세요."
print(string.find("안녕"))
print(string.rfind("안녕"))

# in 연산자
print("안녕" in string)

# 문자열자르기 : split()
a = "10 20 30 40 50".split(" ")
print(a)

print("{}".format(10))
print(f'{10}')
print(f"3 + 7 = {3 + 7}")

x = "hello"
x.upper() # 비파괴적, 기존 x에 할당된 값을 변형시키지 않는다.
print("A 지점 :", x)
print("B 지점 :", x.upper())