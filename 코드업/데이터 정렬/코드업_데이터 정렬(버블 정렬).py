# 코드업_데이터 정렬(버블 정렬)

n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

sort_arr = sorted(arr)

for elem in sort_arr :
    print(elem)