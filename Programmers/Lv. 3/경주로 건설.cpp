#include <string>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>

using namespace std;

// 상 하 좌 우
int moveY[4] = {-1, 1, 0, 0};
int moveX[4] = {0, 0, -1, 1};

int solution(vector<vector<int>> board) {
    int SIZE = board.size();
    
    int prices[25][25][4];
    for (int i = 0; i < 25; i++)
    {
        for (int j = 0; j < 25; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                prices[i][j][k] = 1000000;
            }
        }
    }
    for (int i = 0; i < 4; i++)
    {
        prices[0][0][i] = 0;
    }
    
    // 현재 위치 y, x, 비용 price, 이전 move 방향 direction
    queue<tuple<int, int, int, int>> q;  
    q.push({0, 0, 0, -1});
    
    while (!q.empty())
    {
        auto tmp = q.front();
        q.pop();
        int cy = get<0>(tmp);
        int cx = get<1>(tmp);
        int price = get<2>(tmp);
        int direction = get<3>(tmp);
        
        for (int i = 0; i < 4; i++)
        {
            int ny = cy + moveY[i];
            int nx = cx + moveX[i];
            if (ny >= 0 && ny < SIZE && nx >= 0 && nx < SIZE && board[ny][nx] == 0)
            {
                int tmp_price = price;
                tmp_price += 100;
                if ((direction == 0 || direction == 1) && (i == 2 || i == 3))
                {
                    tmp_price += 500;
                }
                if ((direction == 2 || direction == 3) && (i == 0 || i == 1))
                {
                    tmp_price += 500;
                }

                if (tmp_price < prices[ny][nx][i])
                {
                    prices[ny][nx][i] = tmp_price;
                    q.push({ny, nx, tmp_price, i});   
                }
            }
        }        
    }
    
    int answer = *min_element(prices[SIZE-1][SIZE-1], prices[SIZE-1][SIZE-1]+4);
    return answer;
}