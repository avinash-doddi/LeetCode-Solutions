class Solution:
    def convertToTitle(self, col: int) -> str:
        s = ""
        while col:
            s += chr((col - 1)%26  + ord('A'))
            col = (col-1)//26;
        return s[::-1]