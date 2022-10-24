class Solution:
    def intToRoman(self, num: int) -> str:
        returnstr = ''
        while(num > 0):
            if (num >= 1000):
                returnstr += 'M'; num -= 1000;
            elif (num >= 900):
                returnstr += "CM"; num -= 900;
            elif (num >= 500):
                returnstr += 'D'; num -= 500;
            elif (num >= 400):
                returnstr += "CD"; num -= 400;
            elif (num >= 100):
                returnstr += 'C'; num -= 100;
            elif (num >= 90):
                returnstr += 'XC'; num -= 90;
            elif (num >= 50):
                returnstr += 'L'; num -= 50;
            elif (num >= 40):
                returnstr += 'XL'; num -= 40;
            elif (num >= 10):
                returnstr += 'X'; num -= 10;
            elif (num >= 9):
                returnstr += 'IX'; num -= 9;
            elif (num >= 5):
                returnstr += 'V'; num -= 5;
            elif (num >= 4):
                returnstr += 'IV'; num -= 4;
            elif (num >= 1):
                returnstr += 'I'; num -= 1;
        return returnstr