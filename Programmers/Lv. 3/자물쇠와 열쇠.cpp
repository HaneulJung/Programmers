#include <string>
#include <vector>

using namespace std;

vector<vector<int>> Rotate90(vector<vector<int>> k, int M)
{
    vector<vector<int>> result;
    
    for (vector<int> kk : k)
    {
        result.push_back({kk[1], -kk[0]+M});
    }
    
    return result;
}

bool solution(vector<vector<int>> key, vector<vector<int>> lock) {
    int M = key.size();
    int N = lock.size();
    
    vector<vector<int>> k;
    for (int y = 0; y < M; y++)
    {
        for (int x = 0; x < M; x++)
        {
            if (key[y][x] == 1)
            {
                k.push_back({y, x});
            }
        }
    }
    
    vector<vector<int>> l;
    for (int y = 0; y < N; y++)
    {
        for (int x = 0; x < N; x++)
        {
            if (lock[y][x] == 0)
            {
                l.push_back({y, x});
            }
        }
    }
    int num_zero = l.size();
    
    for (int r = 0; r < 4; r++)
    {
        if (r != 0)
        {
            k = Rotate90(k, M);
        }
        
        for (int j = -M+1; j < N; j++)
        {
            for (int i = -M+1; i < N; i++)
            {
                int cnt = 0;
                for (vector<int> kk : k)
                {
                    int ny = kk[0]+j;
                    int nx = kk[1]+i;
                    if (ny >= 0 && ny < N && nx >= 0 && nx < N)
                    {                        
                        if (lock[ny][nx] == 1)  break;
                        cnt++;
                    }                      
                }
                if (cnt == num_zero)    return true;  
            }
        }
    }
    
    return false;
}