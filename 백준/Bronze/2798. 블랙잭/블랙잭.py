n, m  = map(int, input().split())

numbers = list(map(int, input().split()))

# 세장을 골라서 더한다. 모든 경우의수를 다 ~ 더해서 구한다. m 넘는거 짜른다. 그중 젤 큰수의 조합 뽑는다.
total = []
for i in range(0, len(numbers) - 2):
    for j in range(i + 1, len(numbers) - 1):
        for k in range(j + 1, len(numbers)):
            part_total = numbers[i] + numbers[j] + numbers[k]
            if part_total <= m:
                total.append(numbers[i] + numbers[j] + numbers[k])
            
total.sort(reverse=True)
print(total[0])
