#include <string>
#include <vector>
#include <iostream>
#include <stack>

using namespace std;

struct Node {
    int n;
    int prev = -1;
    int next = -1;    
};

string solution(int n, int k, vector<string> cmd) {
    string answer(n, 'O');
    
    vector<Node*> columns;
    
    for (int i = 0; i < n; i++)
    {
        Node *node = new Node();
        node->n = i;
        
        if (i > 0)
        {
            node->prev = i-1;
        }
        if (i < n-1)            
        {
            node->next = i+1;
        }
        
        columns.push_back(node);
    }
       
    stack<Node*> deleted;
    for (string c : cmd)
    {
        if (c[0] == 'U')
        {
            int move = stoi(c.substr(2));
            while (move--)
            {
                k = columns[k]->prev;
            }
        }
        else if (c[0] == 'D')
        {
            int move = stoi(c.substr(2));
            while (move--)
            {
                k = columns[k]->next;
            }
        }
        else if (c[0] == 'C')
        {
            int prev = columns[k]->prev;
            int next = columns[k]->next;
            
            deleted.push(columns[k]);
            
            if (prev > -1)
            {
                columns[prev]->next = next;    
            }
            
            if (next > -1)
            {
                columns[next]->prev = prev;                
                k = next;
            }
            else
            {
                k = prev;
            }  
        }
        else if (c[0] == 'Z')
        {
            Node *restore = deleted.top();
            deleted.pop();
            
            int n = restore->n;
            int prev = restore->prev;
            int next = restore->next;
            
            if (prev > -1)
            {
                columns[prev]->next = n;    
            }
            
            if (next > -1)
            {
                columns[next]->prev = n;       
            }
        }
    }
    
    while (!deleted.empty())
    {
        Node *node = deleted.top();
        deleted.pop();
        answer[node->n] = 'X';
    }
    
    return answer;
}