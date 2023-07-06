import time

# while True:
#     print(".", end="")

i = 0
while i < 10:
    print(f"{i} 번째 반복입니다.")
    i += 1

# for문과 달리 조건을 활용해서 반복을 사용해야할때 while을 사용하면 좋다.

list_test = [1, 2, 1, 2]
value = 2

while value in list_test:
    list_test.remove(value)

print(list_test)

# number = 0
# target_tick = time.time() + 5
# while time.time() < target_tick:
#     number += 1
# print("5초동안 {}번 반복하였습니다.".format(number))

i = 0
while True:
    print("{}번째 반복입니다.".format(i))
    i += 1

    input_text = input("> 종료하시겠습니까?(y/n) : ")
    if input_text in ["Y", 'y']:
        print("반복을 종료합니다.")
        break

numbers = [5, 15, 6, 20, 7, 25]
for number in numbers:
    if number < 10:
        continue
    print(number)
