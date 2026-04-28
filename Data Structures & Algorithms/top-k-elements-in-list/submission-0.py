class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nbr_count = defaultdict(int)
        for nbr in nums:
            nbr_count[nbr] += 1
        sorted_nbr_count = sorted(nbr_count.items(), key=lambda x:x[1], reverse=True) 
        print(sorted_nbr_count)
        result = list()
        for i in range(k):
            result.append(sorted_nbr_count[i][0])
        return result
