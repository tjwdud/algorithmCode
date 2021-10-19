
def solution(participant, completion):
    hash_map = {}
    temp = 0
    for part in participant:
        hash_map[hash(part)] = part
        
        temp += hash(part)

    for com in completion:
        temp -= hash(com)
    return hash_map[temp]

