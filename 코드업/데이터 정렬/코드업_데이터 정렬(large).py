# 코드업_데이터 정렬(large)

n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

new_arr = sorted(arr)

for elem in new_arr :
    print(elem)