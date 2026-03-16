import heapq
from collections import Counter

class Solution:
    def topKFrequente(self, nums, k):
        
        count = Counter(nums)
        
        heap = []
        
        for num, freq in count.items():
            
            heapq.heappush(heap, (freq, num))
            
            if len(heap) > k:
                heapq.heappop(heap)
                
        result = []
        
        for freq, num in heap:
            result.append(num)
            
        return result