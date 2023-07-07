class Student:
    count = 0 # 클래스 변수
    def __init__(self, name, korean, english, math, science):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math
        self.science = science

        Student.count += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))

    def get_sum(self):
        return self.korean + self.english + self.math + self.science

    def get_average(self):
        return self.get_sum() / 4

    # 아래와 같이 __str__처럼 함수를 선언해두면, 호출하는 쪽에서 str()과 같이 사용할 수 있다.
    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )

    def __eq__(self, other):
        return self.get_sum() == other.get_sum()

    def __ne__(self, other):
        return self.get_sum() != other.get_sum()

    def __gt__(self, other):
        return self.get_sum() > other.get_sum()

    def __ge__(self, other):
        return self.get_sum() >= other.get_sum()

    def __lt__(self, other):
        return self.get_sum() < other.get_sum()

    def __le__(self, other):
        return self.get_sum() <= other.get_sum()

student_a = Student("kim", 87, 98, 88, 95)
student_b = Student("lee", 92, 87, 43, 25)

print()
print("총 {}명의 학생이 생성되었네요.".format(Student.count))