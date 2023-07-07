numbers = [103, 52, 273, 32, 77]
print(max(numbers))
print(min(numbers))
print(sum(numbers))

list_a = [1, 2, 3, 4, 5]
list_reversed = list(reversed(list_a))
print(list_a)
print(list_reversed)  # <list_reverseiterator object at 0x10ce23be0>

for i in reversed(list_a):
    print("> {}".format(i))

temp = reversed([1, 2, 3, 4, 5, 6])
for i in temp:
    print(i)

for i in temp:
    print(i)

example_list = ["요소1", "요소2", "요소3"]
for i in range(len(example_list)):
    print("{}번째 요소는 {}입니다.".format(i, example_list[i]))

print(list(enumerate(example_list)))
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i, value))

example_dictionary = {
    "키A": "값A",
    "키B": "값B",
    "키C": "값C",
}
print("# 딕셔너리의 items() 함수")
print("items() :", example_dictionary.items())
print()

print("# 딕셔너리의 items() 함수와 반복문 결합하기")
for key, value in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, value))

array = []
for i in range(0, 20, 2):
    array.append(i**2)
print(array)

# 리스트 내포 ( list comprehensions )
array2 = [i**2 for i in range(0, 20, 2)]
print(array2)
array_sample = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array_sample if fruit != "초콜릿"]
print(output)

test = (
    "이렇게 입력해도"
    "하나의 문자열로 연결되어"
    "생성됩니다."
)
print(type(test), test)

number = int(input("정수를 입력해주세요 > "))
if number % 2 == 0:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}은(는) 짝수입니다."
    ).format(number, number))
else:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}은(는) 홀수입니다."
    ).format(number, number))

print("--".join(["1", "2", "3", "4"]))

numbers = [1, 2, 3, 4, 5, 6]
r_nums = reversed(numbers) # Return a reverse iterator over the values of the given sequence.
print("reversed_numbers :", r_nums)
print(next(r_nums))
print(next(r_nums))
print(next(r_nums))
print(next(r_nums))
print(next(r_nums))
print(next(r_nums))
