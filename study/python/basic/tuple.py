# 튜플 : 리스트와 비슷한 자료형
tuple_test = (10, 20, 30)
print(tuple_test[0])
print(tuple_test[1])
print(tuple_test[2])

tuple_test_has_one = (10,) # 하나의 요소만을 가지는 튜플을 작성할때는 꼭 ,를 붙여줘야한다.
print(type(tuple_test_has_one))

[a, b] = [10, 20]
(c, d) = (10, 20)
print("a :", a)
print("b :", b)
print("c :", c)
print("d :", d)

tuple_test2 = 10, 20, 30, 40
print("# 괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test2 :", tuple_test2)
print("type(tuple_test2) :", type(tuple_test2))
print()

a, b, c = 10, 20, 30
print("# 괄호가 없는 튜플을 활용한 할당")
print("a :", a)
print("b :", b)
print("c :", c)

a, b = 10, 20
print("# 교환 전 값")
print("a :", a)
print("b :", b)
print()

a, b = b, a
print("# 교환 후 값")
print("a :", a)
print("b :", b)
print()