class Student:
    def __init__(self, name, korean, english, math, science):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math
        self.science = science

    def get_sum(self):
        return self.korean + self.english + self.math + self.science

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )


students = [
    Student("kim", 87, 98, 88, 95),
    Student("lee", 92, 87, 43, 25),
    Student("jang", 87, 88, 65, 87),
    Student("choi", 87, 80, 87, 65),
    Student("seo", 43, 65, 67, 80),
    Student("park", 75, 42, 68, 86)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student.to_string())
