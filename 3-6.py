# Step 1. 주사위 두개 입력 받기 (단, 4, 6, 8, 12, 20)
N, M = map(int, input().split())

# Step 2. 두 눈의 합 중 가장 큰 값 구하기
# (풀이 2)
# 두 눈의 합과 동일한 인덱스의 값을 +1 증가시켜, 해당 두 눈의 합이 나오는 횟수 기록
lst = [0] * (N + M + 2)

for i in range(1, N+1):
    for j in range(1, M+1):
        lst[i+j] += 1

max = 0
for k in lst:
    if max < k:
        max = k

for value, z in enumerate(lst):
    if z == max:
        print(value, end=' ')

# (풀이 1)
# 두 눈의 합을 리스트에 저장
lst = []
cnt = {}

for i in range(1, N+1):
    for j in range(1, M+1):
        a = i + j
        lst.append(a)

# 두 눈의 합이 나오는 횟수 딕셔너리에 기록
for j in lst:
    if j in cnt:
        continue
    else:
        cnt[j] = lst.count(j)

# 딕셔너리 값의 최대값을 가지는 키 값 저장
result = [key for key, value in cnt.items() if value == max(cnt.values())]
