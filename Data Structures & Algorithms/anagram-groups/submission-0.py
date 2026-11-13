class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create dict of word and assign to a group by sorting?
        groups = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in groups:
                groups[sorted_word]+=[word]
            else:
                groups[sorted_word] = [word]
        
        res = []
        for sorted_word, group in groups.items():
            res.append(group)
        
        return res
            