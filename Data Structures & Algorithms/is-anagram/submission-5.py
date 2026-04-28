class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedS = sorted(s)
        sortedT = sorted(t)
        if len(sortedS) != len(sortedT):
            return False
        for i in range(len(sortedS)):
            if sortedS[i] != sortedT[i]:
                return False
        return True