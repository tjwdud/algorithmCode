def solution(board, moves):
    answer = 0
    basket = []
    new_moves = []
    for i in moves:
       new_moves.append(i-1)

    for k in new_moves:
        for i in range(len(board)):
            if board[i][k] == 0:
                continue
            basket.append(board[i][k])
            if len(basket) > 1:
                if basket[-1] == basket[-2]:
                    basket.pop()
                    basket.pop()
                    answer += 2

            board[i][k] = 0
            break
    return answer
