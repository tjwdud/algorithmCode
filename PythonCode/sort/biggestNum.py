def solution(numbers):
    #리스트를 문자열로 바꾼다.
    numbers = list(map(str, numbers))
    #최대 3자릿수 
    numbers.sort(key = lambda x : x*3,reverse=True)
    return str(int(''.join(numbers)))

