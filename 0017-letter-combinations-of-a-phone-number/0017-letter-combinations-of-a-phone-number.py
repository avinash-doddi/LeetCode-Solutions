class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if (digits):
            d = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv",'9':"wxyz"};
            def recur(fin, digits, d, ref):
                if not digits:
                    fin.append(ref); return
                for i in d[digits[0]]:
                    recur(fin, digits[1:], d, ref+i)
            fin = []; ref = ''
            recur(fin, digits, d, ref)
            return fin
        return []
            
            