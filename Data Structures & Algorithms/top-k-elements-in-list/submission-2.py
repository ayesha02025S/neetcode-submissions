class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {} # value : count 
        for num in nums:
            if num not in map:
                map[num] = 1
            map[num] += 1
        
        sort = sorted(map, key=map.get, reverse=True)
        return sort[:k]
        


        