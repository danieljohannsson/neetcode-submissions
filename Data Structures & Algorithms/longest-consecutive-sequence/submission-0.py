class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNumbers = set(nums)
        maxCount = 0
        for nbr in nums:
            count = 1
            right = nbr
            left = nbr
            while right+1 in uniqueNumbers:
                count += 1
                right += 1
            while left-1 in uniqueNumbers:
                count += 1
                left -= 1
            maxCount = max(maxCount, count)

        return maxCount
        