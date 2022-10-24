class Solution:          
    def nthUglyNumber(self, n: int) -> int:
        uglynumbers = [1];
        p1, p2, p3 = 0,0,0;
        while (n > 1):
            m1, m2, m3 = uglynumbers[p1]*2, uglynumbers[p2]*3, uglynumbers[p3]*5;
            minn = min(m1,m2,m3);
            if (minn == m1):p1 += 1;
            if (minn == m2): p2 += 1;
            if (minn == m3): p3 += 1;
            uglynumbers.append(minn);
            n -= 1;
        return uglynumbers[-1]
                