# 함수의 매개변수로 함수를 전달
def call_10_times(func):
    for i in range(10):
        func()

def print_hello():
    print("안녕하세요.")

call_10_times(print_hello)

# map() : 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트를 구성해주는 함수
# filter() : 리스트의 요소를 함수에 넣고 리턴된 값이 True인 것으로, 새로운 리스트를 구성해주는 함수
def power(item):
    return item * item
def under_3(item):
    return item < 3

list_input_a = [1, 2, 3, 4, 5]

output_a = map(power, list_input_a)
print("# map()의 함수 실행 결과")
print("map(power, list_input_a) :", output_a)
print("map(power, list_input_a) :", list(output_a))
print()

output_b = filter(under_3, list_input_a)
print("# filter()의 함수 실행 결과")
print("filter(under_3, list_input_a) :", output_b)
print("filter(under_3, list_input_a) :", list(output_b))
print()

lambda_power = lambda x: x * x
lambda_under_3 = lambda x: x < 3
# lambda_output_a = map(lambda_power, list_input_a)
# print("# [lambda] map()의 함수 실행 결과")
# print("map(lambda_power, list_input_a) :", lambda_output_a)
# print("map(lambda_power, list_input_a) :", list(lambda_output_a))
# print()
lambda_output_a = map(lambda x: x * x, list_input_a)
print("# [lambda] map()의 함수 실행 결과")
print("map(lambda_power, list_input_a) :", lambda_output_a)
print("map(lambda_power, list_input_a) :", list(lambda_output_a))
print()

# lambda_output_b = filter(lambda_under_3, list_input_a)
# print("# [lambda] filter()의 함수 실행 결과")
# print("filter(lambda_under_3, list_input_a) :", lambda_output_b)
# print("filter(lambda_under_3, list_input_a) :", list(lambda_output_b))
# print()
lambda_output_b = filter(lambda x: x < 3, list_input_a)
print("# [lambda] filter()의 함수 실행 결과")
print("filter(lambda_under_3, list_input_a) :", lambda_output_b)
print("filter(lambda_under_3, list_input_a) :", list(lambda_output_b))
print()