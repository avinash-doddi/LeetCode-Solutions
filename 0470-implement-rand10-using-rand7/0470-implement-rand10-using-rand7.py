# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    count = 0;
    def rand10(self):
        """
        :rtype: int
        """
        random = [1,2,3,4,5,6,7,8,9,10]
        self.count += 1; c = 0
        if (self.count & 1):
            for i in range(2,10,2):
                c += i;
            return random[(self.count+c)%10];
        else:
            for i in range(1,9,2):
                c += i;
            return random[(self.count+c)%10];
            