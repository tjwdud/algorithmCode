
def solution(new_id):
    #1단계
    new_id = new_id.lower()
    #2단계
    new_word = ''
    for i in new_id:
        if i.isalnum() or i in '-_.':
            new_word += i
    new_id = new_word
    #3단계
    while '..' in new_id:
        new_id = new_id.replace('..','.')
    #4단계
    if(len(new_id)>0 and new_id[0]=='.'):
        new_id=new_id[1:]
    if(len(new_id)>0 and new_id[-1]=='.'):
        new_id = new_id[:-1]    

    #5단계
    if(len(new_id)==0):
        new_id = 'a'
    #6단계
    if(len(new_id)>15):
        new_id = new_id[:15]
    if(new_id[-1]=='.'):
        new_id = new_id[:-1]
    #7단계

    if(len(new_id)<3):

        while len(new_id)< 3:
            new_id = new_id + new_id[-1]

    answer = new_id
    return answer