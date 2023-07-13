# 프로그래머스 레벨0, 문제 해결 전략 -> 머릿속에서 도무지 직관적으로 생각이 안나서 공식 유도 후 풀었음

def solution(num, total):
    answer = []
    if num % 2 == 1:
        if num == 1:
            answer.append(total)
        else:
            center = total / num
            init = int(center - ((num - 1) / 2))
            last = int(center + ((num - 1) / 2))
            for i in range(init, last + 1):
                answer.append(i)
    else:
        first = int((2 * total - num * num + num) / (2 * num))
        for i in range(first, first + num):
            answer.append(i)
    return answer