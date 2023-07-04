"""
https://www.acmicpc.net/problem/1000

문제를 처음풀어봐서 input이 어떻게 들어오는거지 부터 막혀서 몇번 틀렸다.
보니까 input은 문제에 작성되있는대로 "1 2" 이런식으로 들어와서 input매개변수에 어떤 문자열을 줄 필요가 없음
split() 함수에 매개변수가 2개 들어가는데 여기서는 아무것도 줄 필요가 없는데 그 이유는 split()으로만 사용할 경우 띄어쓰기 및 엔터를 구분자로 문자열을 자르기 때문
print에서 연산할때 int형으로 캐스트 해야하는데 다른 분이 작성하신 소스를 보니 map으로 처리할 수 있어서 아래에 답을 남겨본다.
파이썬 공부 1일차에 아직 map을 보진 못했는데, 공부하고 다시한번 살펴봐야 할듯

a, b = map(int, input().split())
print(a+b)
"""

input = input()
a, b = input.split()
print(int(a) + int(b))
