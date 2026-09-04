class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {} # value : count 

        for n in nums:
            if n not in map:
                map[n] = 1
            map[n] +=1 

        sort = sorted(map, key=map.get, reverse=True)

        return sort[:k]
            

        


        