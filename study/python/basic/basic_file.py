import random

# file = open("./text_sample.txt", "w")
# file.write("Hello Python Programming!!")
# file.close()

# 아래처럼 with 키워드를 사용해서 파일 처리를 하게되면 file.close()를 자동으로 해준다. ( 실수 방지할 수 있음 )
with open("./text_sample.txt", "w") as file:
    file.write("Hello Python Programming!!")

with open("./text_sample.txt", "r") as file:
    contents = file.read()
print(contents)

hanguls = list("가나다라마바사아자차카타파하")
with open("./info.txt", "w") as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)

        file.write("{}, {}, {}\n".format(name, weight, height))

with open("./info.txt", "r") as file:
    for line in file:
        (name, weight, height) = line.strip().split(", ")

        if (not name) or (not weight) or (not height):
            continue

        bmi = int(weight) / ((int(height) / 100) ** 2)
        result = ""

        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"

        print("\n".join([
            "이름: {}",
            "몸무게: {}",
            "키: {}",
            "BMI: {}",
            "결과: {}"
        ]).format(name, weight, height, bmi, result))
        print()