# 난이도: 브론즈 1
# 알고리즘 분류: 수학, 문자열
'''
시작시간: 
종료시간: 
'''

for i in range(3, 0, -1):
    x = input()
    if x not in ['Fizz', 'Buzz', 'FizzBuzz']:
        n = int(x) + i

if n % 15 == 0:
    print('FizzBuzz')
elif n % 3 == 0:
    print('Fizz')
elif n % 5== 0:
    print('Buzz')
else:
    print(n)