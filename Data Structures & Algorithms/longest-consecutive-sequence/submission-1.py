class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNumbers = set(nums)
        maxLength = 0

        for num in uniqueNumbers:
            if (num - 1) not in uniqueNumbers:
                length = 1
                while num+length in uniqueNumbers:
                    length += 1
                maxLength = max(length, maxLength)
        return maxLength
        