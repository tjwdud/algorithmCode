import heapq
def heapsort(iter):
    h = []
    result = []
    for value in iter:
        heapq.heappush(h,value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,5,2,3,4,0])
  
print(result)