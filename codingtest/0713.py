# 약수 구하기 문제 (프로그래머스 레벨0)
def solution(n):
    answer = []

    for i in range(1, n + 1):
        if n % i == 0:
            answer.append(i)
    return answer

inp = int(input())

sol = solution(inp)
print(sol)