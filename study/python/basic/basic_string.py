# python version 확인
# $ python3 -V

# keyword 조회
import keyword
print(keyword.kwlist)

# 자료형 확인
print(type("안녕하세요!"))

# 이스케이프 문자 ( \ )
# \n : 줄바꿈
# \t : 탭
print("\"안녕하세요.\"라고 말했습니다.")
print("name\tage\tlocation")
print("kim\t32\tseoul")
print("lee\t50\tbusan")
print("""동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세""")
# 보기 편하라고 아래와 같이 작성한 경우에는 시작과 끝에 역슬래쉬(\)를 넣어줘야 의도치 않은 개행을 방지할 수 있음.
print("""\
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세\
""")

# 문자열 연결 연산자 ( + ) / 문자열 반복 연산자 ( * )
print("안녕하세요" + "!")
print("안녕하세요\t" * 3)

# 문자 선택 연산자(인덱싱) []
print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[2])
print("안녕하세요"[3])
print("안녕하세요"[4])

# 문자열 범위 선택연산자(슬라이싱) [:]
print("안녕하세요"[0:2])
print("안녕하세요"[:3]) # 안녕하
print("안녕하세요"[2:]) # 하세요

# 문자열 길이 구하기 ( len() )
print(len("안녕하세요."))