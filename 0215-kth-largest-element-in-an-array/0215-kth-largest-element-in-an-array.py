# import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        pq = []

        for num in nums:
            heappush(pq,num)
            while len(pq) > k:
                heappop(pq)
        return pq[0]