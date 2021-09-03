
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i,k in zip(participant,completion):
        if i !=k:
          return i
    return participant.pop()