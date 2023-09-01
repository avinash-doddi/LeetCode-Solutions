class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        from collections import defaultdict as maps
        d = maps(int)
        for i in dictionary: d[i] += 1;
        sentence = sentence.split(' ');
        n = len(sentence)
        for i in range(n):
            tmp = ''
            for char in sentence[i]:
                tmp += char;
                if d[tmp]:
                    break;
            sentence[i] = tmp;
        return " ".join(sentence)

