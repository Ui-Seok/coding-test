# 난이도: 브론즈 4
# 알고리즘 분류: 수학, 문자열, 사칙연산
'''
시작시간: 
종료시간: 
'''

a = int(input())
b = input()
c = int(input())

len_b = len(b)
b = int(b)

i_num = a + b - c
s_num = a * (10 ** len_b) + b - c

print(i_num)
print(s_num)