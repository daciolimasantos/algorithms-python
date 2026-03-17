class Solution:
    def jump(self, nums):
        
        steps = 0
        end = 0
        farthest = 0
        
        for i in range(len(nums) - 1):
            
            farthest = max(
                farthest,
                i + nums[i]
            )
            
            if i == end:
                
                steps += 1
                end = farthest
                
        return steps