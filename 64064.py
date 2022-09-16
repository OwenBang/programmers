def solution(board, moves):
    answer = 0
    bucket = []
    for i in moves:
        temp = 0
        while True:
            if board[temp][i-1] == 0:
                temp += 1
                if temp == len(board):
                    break
            else:
                bucket.append(board[temp][i-1])
                if len(bucket) >= 2:
                    if bucket[-1] == bucket[-2]:
                        del bucket[-1]
                        del bucket[-1]
                        answer += 2
                board[temp][i-1] = 0
                break
            
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
moves = [1,5,3,5,1,2,1,4]	
print(solution(board, moves))