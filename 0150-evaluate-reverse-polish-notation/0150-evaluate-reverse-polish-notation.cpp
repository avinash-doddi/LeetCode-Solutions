class Solution {
public:
   long long int evalRPN(vector<string>& tokens) {
        long long int n=tokens.size();
        stack<long long int> st;
        for(auto a:tokens){
            if(a!="+" && a!="-" && a!="*" && a!="/") st.push(stoi(a));
            else{
                long long int top1=st.top();
                st.pop();
                long long int top2=st.top();
                st.pop();
                if(a=="+") st.push(top1+top2);
                else if(a=="-") st.push(top2-top1);
                else if(a=="*") st.push(top2*top1);
                else st.push(top2/top1);
            }
        }
        return st.top();
    }
};