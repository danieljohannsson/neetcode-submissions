class Solution:
    def maxArea(self, heights: List[int]) -> int:
        firstIdx = 0
        lastIdx = len(heights)
        maxVol = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i != j:
                    maxVol = max(maxVol, abs(i-j)* min(heights[i], heights[j]))
        return maxVol                