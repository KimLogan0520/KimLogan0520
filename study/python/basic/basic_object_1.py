# import random as r
#
# def get_random_name_and_score():
#     hanguls = list("가나다라마바사아자차카타파하")
#
#     return {
#         "name": r.choice(hanguls) + r.choice(hanguls) + r.choice(hanguls),
#         "korean": r.randrange(80, 100),
#         "english": r.randrange(80, 100),
#         "math": r.randrange(80, 100),
#         "science": r.randrange(80, 100)
#     }
#
# students = [
#     get_random_name_and_score(),
#     get_random_name_and_score(),
#     get_random_name_and_score(),
#     get_random_name_and_score(),
# ]
#
# print("이름", "총점", "평균", sep="\t")
# for student in students:
#     sum = student["korean"] + student["english"] + student["math"] + student["science"]
#     average = sum / 4
#     print(student["name"], sum, average, sep="\t")

def create_student(name, korean, english, math, science):
    return {
        "name": name,
        "korean": korean,
        "english": english,
        "math": math,
        "science": science
    }


def student_get_sum(student):
    return student["korean"] + student["english"] + student["math"] + student["science"]


def student_get_average(student):
    return student_get_sum(student) / 4


def student_to_string(student):
    return "{}\t{}\t{}".format(
        student["name"],
        student_get_sum(student),
        student_get_average(student)
    )


students = [
    create_student("kim", 87, 98, 88, 95),
    create_student("lee", 92, 87, 43, 25),
    create_student("jang", 87, 88, 65, 87),
    create_student("choi", 87, 80, 87, 65),
    create_student("seo", 43, 65, 67, 80),
    create_student("park", 75, 42, 68, 86),
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student_to_string(student))
