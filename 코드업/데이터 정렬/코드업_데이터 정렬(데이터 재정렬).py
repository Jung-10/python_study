# 코드업_데이터 정렬(데이터 재정렬)

n = int(input())

arr = list(map(int, input().split()))

first_arr = arr

class Number :
    def __init__(self, number, idx):
        self.number = number
        self.idx = idx

arr = sorted(arr)

arr_sort = []

for i in range(n) :
    number = arr[i]
    arr_sort.append(Number(number, i))

result = []

for i in range(n) :
    for j in range(n) :
        if first_arr[i] == arr_sort[j].number :
            result.append(arr_sort[j].idx)

for elem in result :
    print(elem, end = " ")