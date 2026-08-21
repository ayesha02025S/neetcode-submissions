class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} # sorted val : list of words
        for word in strs:
            sort = tuple(sorted(word))
            if sort not in anagrams:
                anagrams[sort] = []
            anagrams[sort].append(word)
        return list(anagrams.values())
        