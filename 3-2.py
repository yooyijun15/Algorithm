# Step 1. 실행 횟수 T 입력 받기
T = int(input())

# Step 2. 입력받은 리스트의 s번째부터 e까지 정렬하고 K번째 수 출력하기
for i in range(T):
    # N : 리스트 원소 개수
    # s,e : s번째부터 e까지
    # K : 출력할 수의 번호
    N, s, e, K = map(int, input().split())
    # 리스트 입력받기
    a = list(map(int, input().split()))
    # s번째부터 e까지 정렬
    a = a[s-1:e]
    a.sort()
    # 정렬된 리스트의 K번째 수 출력
    print(f"#{i+1} {a[K-1]}")
