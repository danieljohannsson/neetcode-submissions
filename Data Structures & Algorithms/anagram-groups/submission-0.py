class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramSet = set()
        anagramDict = dict()
        for s in strs:
            sortedString = ''.join(sorted(s))
            if sortedString in anagramSet:
                wordList = anagramDict.get(sortedString)
                wordList.append(s)
                anagramDict[sortedString] = wordList
            else:
                anagramDict[sortedString] = [s]
                anagramSet.add(sortedString)
        result = []
        for v in anagramDict.values():
            result.append(v)
        return result

        