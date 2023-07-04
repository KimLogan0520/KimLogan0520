array = ["kim", "chan", 32, True, False]
print(array)

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(list_a)
print(list_b)

list_a_with_b = list_a + list_b
print(list_a_with_b)
print(list_a*3)
print(len(list_a))

list_c = [1, 2, 3]
list_c.append(4)
list_c.append(5)
print(list_c)

list_c.insert(0, 99)
print(list_c)

list_d = [1, 2, 3]
list_d.extend([4, 5, 6])
print(list_d)

del list_d[0] # <== 이곳에 슬라이싱 사용 가능
print(list_d)

list_d.pop(0) # pop의 매개변수로 아무것도 주지않으면 -1이 들어가서 맨 끝에 있는 요소를 삭제한다.
print(list_d)

print()
list_e = [1, 2, 1, 2]
list_e.remove(2) # 가장 먼저 발견되는 2 하나만 삭제한다.
print(list_e)

list_e.clear()
print(list_e)

print()
list_f = [3, 44, 12, 9, 80, 34]
list_f.sort()
print(list_f)

list_f.sort(reverse=True)
print(list_f)

print()
list_g = [3, 99, 38]
print(3 in list_g)
print(44 not in list_g)
