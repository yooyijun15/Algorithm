# Step 1. 리스트 a 입력 받기
a = list(map(int,input().split()))
min = float('inf')
# 'inf' : 매우 큰 값

# Step 2. 리스트 a의 원소 중 최소값 min에 넣기
for i in range(len(a)):
    if a[i] < min:
        min = a[i]

# Step 3. 최소값 출력하기
print(min)
