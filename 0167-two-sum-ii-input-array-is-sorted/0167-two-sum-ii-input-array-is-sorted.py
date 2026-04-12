class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        dic = {}
        for i,c in enumerate(numbers):
            complement = target - c
            if complement not in dic:
                dic[c] = i
            else:
                return[dic[complement]+1,i+1]
