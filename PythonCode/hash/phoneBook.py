def solution(phone_book):
    answer = True
    phone_book.sort()
    if len(phone_book) == 1:
        return answer
    else:
        while answer == True:
            for i in range(len(phone_book)-1):
                if phone_book[i] in phone_book[i+1][:len(phone_book[i])]:
                    answer = False
                    break
            break
    return answer