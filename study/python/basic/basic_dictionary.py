# 리스트는 인덱스를 기반으로 값을 저장, []
# 딕셔너리는 키를 기반으로 값을 저장, {}

dict_a = {
    "name": "test name",
    "type": "movie",
    "inner_dict": {
        "inner_name": "inner test name",
        "inner_type": "inner test type"
    },
    "inner_list": [1, 2, 3, 4, 5]
}
print(dict_a["inner_dict"]["inner_type"])
print(dict_a["inner_list"][0])

# 딕셔너리에 값 추가하기
dict_a["added_key"] = 999
print(dict_a)

# 딕셔너리에서 값 제거하기
del dict_a["added_key"]
print(dict_a)

dict_b = {}
print("요소 추가 이전 :", dict_b)

dict_b["name"] = "새로운 이름"
dict_b["head"] = "새로운 정신"
dict_b["body"] = "새로운 몸"
print("요소 추가 이후 :", dict_b)

# key = input("접근하고자 하는 키 > ")
# if key in dict_b:
#     print(f'{key}는 존재합니다. 값 : {dict_b[key]}')
# else:
#     print(f'존재하지 않는 {key}값에 접근하려합니다.')

value = dict_b.get("존재하지 않는 키")
print(value)

if value == None:
    print("존재하지 않는 키에 접근했습니다.")

for key in dict_b:
    print(key, ":", dict_b[key])