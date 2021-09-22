#가장 직관적인 형태의 퀵소트
array= [ 5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick(array,start,end):
    #재귀함수니까 종료조건 먼저 써준다
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        #피벗보다 큰 수를 찾을때까지(작거나 같을 때만 while문)
        while left <= end and array[left] <= array[pivot]:
            left += 1
        #피벗보다 작은 수를 찾을때까지
        while right > start and array[right] >= array[pivot]:
            right -= 1
        #엇갈렸다면 작은 데이터와 피벗을 교체
        if left > right:
          #작은 데이터는 오른쪽 인덱스에 위치해있다.
            array[right],array[pivot] = array[pivot],array[right]
        #엇갈리지 않았다면 작은 큰 바꾼다.
        else:
            array[right],array[left] = array[left],array[right]
        
        quick(array,start,right-1)
        quick(array,right+1,end)
    print(array)

quick(array,0,len(array)-1)