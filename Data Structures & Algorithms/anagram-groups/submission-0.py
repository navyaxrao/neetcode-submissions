class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {} # {sorted_word, [list of all anagrams of word]}
        for word in strs:
            sorted_word = str(sorted(word))
            if sorted_word in hmap:
                hmap[sorted_word].append(word)
            else:
                hmap[sorted_word] = [word]
        return list(hmap.values())

        