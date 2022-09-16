def solution(n):
    answer = 0
    temp = str(n)
    for i in temp:
        answer += int(i)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print(temp)

    return answer