import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        answer = []
        q = []
        for i in arr:
            heapq.heappush(q, [abs(i-x), i])
        
        for i in range(k):
            _, el = heapq.heappop(q)
            answer.append(el)
        
        answer.sort()
        
        return answer
