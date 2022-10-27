from collections import defaultdict as maps
class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        reference = maps(list)
        for word in s:
            reference[tuple(sorted(word))].append(word)
        return reference.values()
                
        
