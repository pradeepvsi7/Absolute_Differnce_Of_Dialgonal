def dig(arr):
	sum1 = sum([arr[x][x] for x in range(len(arr))])
	sum2 = sum([arr[x][n-1-x] for x in range(len(arr))])
	diff = abs(sum1-sum2)
	return diff



n = int(input())
arr = []
for _ in range(n):
	arr.append(list(map(int,input().strip().split())))
result = dig(arr)
print(result)



