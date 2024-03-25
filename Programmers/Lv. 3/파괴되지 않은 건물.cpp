#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board, vector<vector<int>> skill) {
    int answer = 0;
    
    int N = board.size();
    int M = board[0].size();
    
    vector<vector<int>> sum(N+1, vector<int>(M+1, 0));
        
    for (vector<int> sk : skill)
    {
        int type = sk[0];
        int r1 = sk[1];
        int c1 = sk[2];
        int r2 = sk[3];
        int c2 = sk[4];
        int degree = type == 1 ? -sk[5] : sk[5];
        
        sum[r1][c1] += degree;
        sum[r1][c2+1] -= degree;
        sum[r2+1][c1] -= degree;
        sum[r2+1][c2+1] += degree;
    }
    
    for (int r = 0; r < N+1; r++)
    {
        for (int c = 1; c < M+1; c++)
        {
            sum[r][c] += sum[r][c-1];
        }
    }
    
    for (int c = 0; c < M+1; c++)
    {
        for (int r = 1; r < N+1; r++)
        {
            sum[r][c] += sum[r-1][c];
        }
    }
    
    for (int r = 0; r < N; r++)
    {
        for (int c = 0; c < M; c++)
        {
            if (board[r][c] + sum[r][c] > 0)
            {
                answer++;
            }
        }
    }
    
    return answer;
}