def print_3_times():
    print("안녕하세요.")
    print("안녕하세요.")
    print("안녕하세요.")


print_3_times()

"""
가변 매개변수
"""


def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)


print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")


def print_n_times2(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)

# 가변매개변수와 기본매개변수를 같이 쓰는 경우
# 무조건 가변매개변수가 먼저 작성되어야하고, 기본 매개변수는 키워드매개변수로 아래처럼 n=3 과 같이 작성해주어야 한다.
# print_n_times2("안녕하세요.", "즐거운", "파이썬 프로그래밍", 3)처럼 호출하게되면, 함수 정의에 작성되어있는 것처럼 두번만 반복됨
print_n_times2("안녕하세요.", "즐거운", "파이썬 프로그래밍", n=3)

def test(a, b=10, c=100):
    print(a + b + c)

test(10, 20, 30)
test(a=10, b=20, c=30)
test(c=30, a=10, b=20)
test(10, c=40)

def return_test():
    print("A의 위치입니다.")
    return
    print("B의 위치입니다.")
return_test()

def return_test2():
    return 100
value = return_test2()
print(value)

def sum_all(start, end):
    output = 0
    for i in range(start, end+1):
        output += i

    return output
value2 = sum_all(1, 3)
print(value2)

def mul(*values):
    output = 1
    for value in values:
        output *= value
    return output
print(mul(5, 7, 9, 10))

def factorial(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    # for i in range(n, 0, -1):
    #     output *= i
    return output
print(factorial(3))

def factorial2(n):
    if n == 0:
        return 1

    return n * factorial2(n-1)
print(factorial2(3))

def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(4))
# print(fibonacci(35))

counter = 0
def fibonacci2(n):
    print("fibonacci({})를 구합니다.".format(n))
    global counter
    counter += 1

    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci2(n-1) + fibonacci2(n-2)

fibonacci2(10)
print("---")
print("fibonacci(10) 계산에 활용된 덧셈의 횟수는 {}번입니다.".format(counter))

# 메모화
# dictionary에 미리 계산된 값을 보관해서 필요할때마다 꺼내서 사용 ( 재귀함수 사용시 많이 사용됨 )
dictionary = {
    1: 1,
    2: 1
}
def fibonacci3(n):
    if n in dictionary:
        return dictionary[n]

    output = fibonacci3(n-1) + fibonacci3(n-2)
    dictionary[n] = output
    return output

print(fibonacci3(10))
print(fibonacci3(20))
print(fibonacci3(30))
print(fibonacci3(40))
print(fibonacci3(50))
print(dictionary)

def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            output.append(item)
    return output
example_data = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본 :", example_data)
print("변환 :", flatten(example_data))