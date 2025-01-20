# Step 1. 학생 수 N, 점수 입력 받기
N = int(input())
scores = list(map(int, input().split()))
# for x in range(N):
#     a = int(input())
#     list.append(a)

# Step 2. 평균 구하기
avg = int(round(sum(scores) / N, 0))


# Step 3. 평균과 가장 인접한 점수 및 학생 구하기
# - 차이 동일할 경우, 높은 점수 출력
# - 점수 동일할 경우, 인덱스 낮은 점수 출력
avg_differ = 1000

for i, score in enumerate(scores):
    differ = abs(avg - score)
    if differ < avg_differ:
        avg_differ = differ
        avg_stu = i+1
        avg_stu_score = score
    elif avg_differ == differ:
        if avg_stu_score < score:
            avg_stu = i+1
            avg_stu_score = score

print(avg, avg_stu)
