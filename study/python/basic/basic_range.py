# 리스트, 딕셔너리 외에 for문과 함꼐 많이 사용되는 range()

# range(A) : 0 부터 A-1 까지 반복
for num in range(3):
    print(num)

# range(A, B) : A 부터 B-1까지 반복
for num in range(3, 7):
    print(num)

# range(A, B, C) : A 부터 B-1까지 반복하는데, C만큼 건너뛰어 반복
for num in range(0, 10, 2):
    print(num)

num_list = list(range(0,5))
print(num_list)

n = 10
num_list2 = list(range(0, n//2))
print(num_list2)

for i in range(5):
    print(i)

array = [399, 2331, 293, 235, 839]
for i in array:
    print(i)
print()
for i in range(len(array)):
    print("{}번째 반복 : {}".format(i+1, array[i]))

# 역반복문
for i in range(4, 0-1, -1):
    print("현재 반복 변수 : {}".format(i))

for i in reversed(range(5)):
    print("현재 반복 변수 : {}".format(i))

# 별찍기
for i in range(9):
    row = ""
    for j in range(i+1):
        row += "*"
    print(row)

output = ""
for i in range(1, 15):
    for j in range(14, i, -1):
        output += " "
    for k in range(0, 2*i-1):
        output += "*"
    output += "\n"
print(output)
#             *
#            ***
#           *****
#          *******
#         *********
#        ***********
#       *************
#      ***************
#     *****************
#    *******************
#   *********************
#  ***********************
# *************************
#***************************

