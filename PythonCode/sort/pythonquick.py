#파이썬의 장점을 살린 퀵소트
array= [ 5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quicksort(array):
    #리스트가 하나의 데이터만 가지고 있으면 종료
    if len(array) <= 1:
        return array
    pivot = array[0]
    #피벗을 제외한 리스트
    tail = array[1:]

    #분할된 왼쪽 부분
    #피벗과 같거나 작은 수 모두 왼쪽에 
    left_side = [x for x in tail if x <= pivot]
    #피벗보다 큰 수는 모두 오른쪽에
    right_side = [x for x in tail if x > pivot]
    print(left_side,pivot,right_side)
    #분할 이후 왼쪽 오른쪽 각각 정렬 수행후 전체 리스트 반환
    return quicksort(left_side) + [pivot] + quicksort(right_side)


print(quicksort(array))