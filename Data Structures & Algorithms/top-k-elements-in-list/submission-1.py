class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for nbr in nums:
            count[nbr] += 1

        keys = sorted(count.items(), key=lambda item: item[1], reverse=True)
        print(keys)
        result = []
        for i in range(k):
            result.append(keys[i][0])
        return result