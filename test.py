ls1 = [10, 20, 30]
ls2 = [1, 2, 3]

result = list(map(lambda num: '홀수' if num % 2 else "짝수", ls2))
print(result)
