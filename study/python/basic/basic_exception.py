"""
오류 error
  - 실행전
    - 구문 오류 syntax error
  - 실행중
    - 예외 exception
    - 런타임 오류 runtime error

예외를 처리하는 방법
    1. 조건문으로 처리
    2. try구문을 사용
"""
# 조건문을 사용한 예외처리
# user_input_a = input("정수 입력 > ")
# if user_input_a.isdigit():
#     number_input_a = int(user_input_a)
    # print("==> number_input_a :", number_input_a)
# else:
#     print("정수를 입력하지 않았습니다.")

# try except 구문을 사용한 예외처리
try:
    number_input_a = int(input("정수 입력 > "))
    print("==> number_input_a :", number_input_a)
except:
    # print("무언가가 잘못됬네요.")
    pass
print("========================= here!")

list_input_a = ["52", "273", "32", "스파이", "103"]
list_numbers = []
for item in list_input_a:
    try:
        float(item)
        list_numbers.append(float(item))
    except:
        pass
print("============> list_numbers :", list_numbers)

"""
try
    예외가 발생할 수 있는 코드
except
    예외가 발생했을때 실행할 코드
else
    예외가 발생하지 않았을때 실행할 코드
finally
    무조건 실행할 코드
"""
try:
    number_input_a = int(input("정수 입력 > "))
except:
    pass
else:
    print("=======> number_input_a :", number_input_a)
finally:
    print("===========> in finally!! ")

try:
    file = open("info.txt", "w")
    file.close()
except:
    print("오류가 발생했습니다.")

print("파일이 제대로 닫혔는지 확인하기.")
print("file.closed() :", file.closed)

def write_text_file(filename, text):
    try:
        file = open(filename, "w")
        return
        file.write(text)
    except:
        print("오류가 발생했습니다.")
    finally:
        file.close()

write_text_file("text.txt", "안녕하세요!")

print("\n프로그램이 시작되었습니다!")
while True:
    try:
        print("try 구문이 시작되었습니다.")
        break
        print("try 구문의 break 뒤입니다.")
    except:
        print("오류가 발생하였습니다.")
    finally:
        print("finally 구문이 시작되었습니다.")

    print("while 반목문의 마지막 줄입니다.")

print("프로그램이 종료되었습니다.")

"""
exception object 예외 객체
try:
    예외가 발생할 가능성이 있는 구문
except 예외의 종류 as 예외 객체를 활용할 변수 이름:
    예외가 발생했을때 실행할 구문
"""
try:
    number_input_a = int(input("정수 입력 > "))
    print("=======> number_input_a :", number_input_a)
except Exception as exception:
    print("type(exception) :", type(exception))
    print("exception :", exception)

list_number = [52, 273, 32, 72, 100]
try:
    input_num = int(input("정수 입력 >> ")) # ValueError 발생 가능
    print("{}번째 요소 : {}".format(input_num, list_number[input_num])) # IndexError 발생 가능
except ValueError as exception:
    print("ValueError 발생")
    print("exception :", exception)
except IndexError as exception:
    print("IndexError 발생")
    print("exception :", exception)
except Exception as exception:
    print("Exception 발생")
    print("exception :", exception)

# 일부러 예외를 발생시킬때 쓰는 키워드 : raise
