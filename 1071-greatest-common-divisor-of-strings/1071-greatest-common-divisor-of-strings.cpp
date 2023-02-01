class Solution {
public:
    string gcdOfStrings(string a, string b) {
        if(a + b == b + a){
            return a.substr(0, gcd(a.length(), b.length()));
        }
        return "";
        
    }
};