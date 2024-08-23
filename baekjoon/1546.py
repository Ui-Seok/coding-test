# 난이도: 
# 알고리즘 분류: 
'''
시작시간: 
종료시간: 
'''

n = int(input())

score = list(map(int, input().split()))

max_score = max(score)
sum_score = sum(score)
avg_score = (sum_score / max_score * 100) / n

print(avg_score)