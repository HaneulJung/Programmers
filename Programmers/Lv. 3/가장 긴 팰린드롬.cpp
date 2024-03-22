#include <iostream>
#include <string>
using namespace std;

string s;
int answer = 1;
int str_length = 0;

void IsPalindrome(int begin, int end)
{
    while (begin >= 0 && end < str_length) 
    {
		if (s[begin] != s[end]) {
			break;
		}
		begin--;
		end++;
	}
    
    answer = max(answer, end-begin-1);
}

int solution(string s_)
{
    s = s_;
    str_length = s.length();
    
    for (int i = 0; i < str_length; i++)
    {
        IsPalindrome(i, i);
        IsPalindrome(i, i+1);
    }
    
    return answer;
}