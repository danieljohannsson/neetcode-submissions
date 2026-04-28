class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        index_value = {}

        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in index_value:
                j = index_value[remainder]
                if j > i:
                    return [i, j]
                else:
                    return [j, i]
            else:
                index_value[nums[i]] = i
            print(index_value)
        return []