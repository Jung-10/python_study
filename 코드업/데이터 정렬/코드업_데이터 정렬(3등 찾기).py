# 코드업_데이터 정렬(3등 찾기)

n = int(input())

class Student :
    def __init__(self, name, score) :
        self.name = name
        self.score = score

score_result = []

for _ in range(n) :
    name, score = list(input().split())
    score_result.append(Student(name, int(score)))

score_result.sort(key=lambda x : -x.score)

print(score_result[2].name)
