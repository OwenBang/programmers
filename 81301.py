def solution(s):
    answer = 0
    i = 0
    while True:
        try:
            temp = int(s[i])
            i += 1
        except:
            if s[i] == "z":
                temp = 0
                i += 4
            elif s[i] == "o":
                temp = 1
                i += 3
            elif s[i] == "t":
                if s[i+1] == "w":
                    temp = 2
                    i += 3
                else:
                    temp = 3
                    i += 5
            elif s[i] == "f":
                if s[i+1] == "o":
                    temp = 4
                    i += 4
                else:
                    temp = 5
                    i += 4
            elif s[i] == "s":
                if s[i+1] == "i":
                    temp = 6
                    i += 3
                else:
                    temp = 7
                    i += 5
            elif s[i] == "e":
                temp = 8
                i += 5
            else:
                temp = 9
                i += 4
        answer = answer * 10 + temp
        if i == len(s):
            break
    return answer

s = "one4seveneight"	
print(solution(s))