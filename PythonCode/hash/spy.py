
def solution(clothes):
    answer = 1
    types = []
    dic = {}
    #옷 종류 
    for i,j in clothes:
        types.append(j)
    types = list(set(types))
    #옷 종류 별 갯수 0으로 초기화
    for i in types:
        dic[hash(i)] = 0
    #종류별 옷 갯수 구하기
    for i,j in clothes:
        dic[hash(j)] +=1
    for k in dic:
        answer *= dic[k]+1
    
    return answer-1

print(solution([['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7'], ['8', '8'], ['9', '9'], ['10', '10'], ['11', '11'], ['12', '12'], ['13', '13'], ['14', '14'], ['15', '15'], ['16', '16'], ['17', '17'], ['18', '18'], ['19', '19'], ['20', '20'], ['21', '21'], ['22', '22'], ['23', '23'], ['24', '24'], ['25', '25'], ['26', '26'], ['27', '27'], ['28', '28'], ['29', '29'], ['30', '30']]))

'''
['a','A'],['b','B'],['c','A'],['d','C'],['e','D']
'''