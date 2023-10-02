class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = 0; bob = 0; cnt = 0
        for i in colors:
            if i == 'A':
                cnt += 1;
            else:
                if cnt >= 3:
                    alice += (cnt - 2);
                cnt = 0;
        if cnt >= 3:
            alice += (cnt - 2);
        cnt = 0;
        for i in colors:
            if i == 'B':
                cnt += 1;
            else:
                if cnt >= 3:
                    bob += (cnt - 2);
                cnt = 0;
        if cnt >= 3:
            bob += (cnt - 2);
        print(alice, bob)
        return False if (alice <= bob) else True
            
        
                
        