# 코드업_데이터 정렬(내림차순 정렬)

n = int(input())

arr = list(map(int, input().split()))

new_arr = sorted(arr)

for elem in new_arr[::-1] :
    print(elem, end = " ")