class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.replace(" ","_")
        num = '0123456789'; pos = (2**31) - 1; neg = -2**31
        minus = 0; final = '';
        for char in s:
            if minus:
                if char == '_':
                    if final:break
                    else: continue;
                elif char == '.':break;
                elif char == '+': 
                    if final:break;
                    else: 
                        final = '0';continue;
                elif char == '-':
                    if final:break;
                    else: 
                        minus = 1; continue;
                elif char in num:
                    final += char;
                else:break;
            else:
                if char == '_':
                    if final:break
                    else: continue;
                elif char == '.':break;
                elif char == '+': 
                    if final:break;
                    else:
                        final = '0';continue;
                elif char == '-':
                    if final:break;
                    else: 
                        minus = 1; final = "0"; continue;
                elif char in num:
                    final += char;
                else:break;
        if minus:
            final = -(int(final)) if final else 0;
            if final < neg: final = neg;
        else: 
            final = int(final) if final else 0;
            if final > pos: final = pos;
        return final