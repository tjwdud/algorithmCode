def solution(citations):
    index = len(citations) 
    while index >=0:
        #리스트에서 index값 이상이면 값 넣기 
        rarray = [x for x in citations if index <= x]
        #인덱스 이상값만 넣은 리스트 길이가 리스트 이상이면 
        #최대 h_index
        if len(rarray) >= index:
            return index
        #아니면  1빼고 반복
        else:
            index -= 1
    return 
