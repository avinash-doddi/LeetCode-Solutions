from bisect import bisect_right as upper_bound
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = upper_bound(letters, target);
        if (index == len(letters)): return letters[0];
        else: return letters[index]