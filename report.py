def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    report_set = set(report)
    report = list(report_set)
    print(report)
    report_cnt = [0 for i in range(len(id_list))]
    print(report_cnt)
    for i in report:
        temp = i.split()
        for j in range(len(id_list)):
            if temp[1] == id_list[j]:
                report_cnt[j] += 1
                break
    print(report_cnt)
    for i in range(len(report_cnt)):
        if report_cnt[i] >= k:
            for j in report:
                temp = j.split()
                if temp[1] == id_list[i]:
                    for k in range(len(id_list)):
                        if id_list[k] == temp[0]:
                            answer[k] += 1
                            break
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))




def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    report_set = set(report)
    report = list(report_set)
    
    report_cnt = [0 for i in range(len(id_list))]
    
    for i in report:
        temp = i.split()
        for j in range(len(id_list)):
            if temp[1] == id_list[j]:
                report_cnt[j] += 1
                break
    
    for i in range(len(report_cnt)):
        for j in report:
            temp = j.split()
            if report_cnt[i] >= k and temp[1] == id_list[i]:
                for 
                            
    return answer