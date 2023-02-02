class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = collections.defaultdict(lambda : 0)
        for element in nums:
            dictionary[element] += 1
        
        dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in dictionary][:k]
