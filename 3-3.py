# Step 1. N, K 입력 받기
N, K = map(int, input().split())

# Step 2. N개의 요소를 갖는 리스트 a 입력 받기
a = list(map(int, input().split()))
# for x in range(N):
#     a = int(input())
#     list.append(a)

sum_set = set()
# set() : 중복 허용하지 않고, 순서 없는 집합 자료형

# Step 3. 리스트 a에서 서로 다른 3개의 원소를 더한 값을 sum_pocket에 원소로 넣기
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_set.add(a[i] + a[j] + a[k])

# Step 4. 리스트 변환 및 내림차순 정렬하기
sum_list = list(sum_set)
sum_list.sort(reverse=True)
# .sort(reverse=True) : 내림차순

# Step 5. K번째 큰 수 출력하기
print(sum_list[K-1])
