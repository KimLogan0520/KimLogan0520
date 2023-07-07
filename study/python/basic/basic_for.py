# for 반복자 in 반복할 수 있는 것 :
#   코드

# array = [3, 33, 88, 23, 51]
# for element in array:
#     print(element)

list_in_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]
for ele in list_in_list:
    for inner_ele in ele:
        print(inner_ele)

# 전개연산자 사용 예제
b = [1, 2, 3, 4]
c = [*b, 5]
print(b)
print(c)