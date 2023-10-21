class Solution:
    def solveEquation(self, eqn: str) -> str:
        if eqn == "x=x": return "Infinite solutions"

        x1 = ""; x2 = ""
        n1 = ""; n2 = ""
        flg = ""
        e = 0; coeff = "";
        n = len(eqn); i = 0;
        while i < n:
            if e: # after "="
                
                if eqn[i] == "x":
                    if coeff:
                        x2 = x2 + flg + coeff; coeff = ""
                    else:
                        x2 = x2 + flg + "1";
                elif 48 <= ord(eqn[i]) <= 57:
                    if i < n-1:
                        temp = ""; xfound = 0
                        while i < n and eqn[i] not in ['+','-']:
                            if eqn[i] == 'x':
                                xfound = 1;
                                coeff = temp; temp = ""; break;
                            temp += eqn[i];  i += 1;
                        if not xfound: 
                            n2 = n2 + flg + temp;
                        i -= 1;
                    else: n2 = n2 + flg + eqn[i];           
                else:
                    flg = eqn[i];     
            else:           
                if eqn[i] == "=": 
                    e = 1; flg = ""
                    
                elif eqn[i] == "x":
                    if coeff:
                        x1 = x1 + flg + coeff; coeff = ""
                    else: x1 = x1 + flg + "1";

                elif 48 <= ord(eqn[i]) <= 57:
                    if i < n-1:
                        temp = ""; xfound = 0
                        while i < n and eqn[i] not in ['+','-', "="]:
                            if eqn[i] == 'x':
                                xfound = 1;
                                coeff = temp; temp = ""; break;
                            temp += eqn[i];  i += 1;
                        if not xfound:
                            n1 = n1 + flg + temp;
                        i -= 1;
                    else: n1 = n1 + flg + eqn[i];
                else:
                    flg = eqn[i];
            i += 1;
        
        # now evaluate thus formed eqn's::
        if not x1: x1 = "0"
        if not x2: x2 = "0"
        if not n1: n1 = "0"
        if not n2: n2 = "0"
            
        x = eval(x1) - eval(x2)
        num = eval(n2) - eval(n1)
        
        print(x1, x2, n1, n2, x,num)
        if not x and not num: return "Infinite solutions"
        if not x: return "No solution"
        
        return "x="+ str(num//x)
        