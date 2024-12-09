# Step 1. N, K 입력 받기
N, K = map(int, input().split())
# input() : 입력 받기
# .split() : 공백을 기준으로 나누기
# map(함수, 객체) : 반복 가능한 객체의 모든 요소에 지정된 함수 적용한 결과 반환

# Step 2. N의 약수 중 K번째로 작은 약수 구하기
# (풀이 2)
cnt = 0
# for-else
for i in range(1, N+1):
    if N % i == 0:
        cnt += 1
    if cnt == K:
        print(i)
        break
else:
    print(-1)

# (풀이 1)
list = []
cnt = 0

for i in range(1, N+1):
    if N % i == 0:
        cnt += 1
        list.append(i)

if K > cnt:
    print(-1)
else:
    print(list[K-1])
