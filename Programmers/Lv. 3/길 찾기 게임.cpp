#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Tree
{
    int idx, x, y;
    Tree *left, *right;
};

bool cmp(Tree* a, Tree* b)
{
    if (a->y == b->y)
    {
        return a->x < b->x;
    }
    return a->y > b->y;
}

void Make_Tree(Tree *root, Tree *child)
{
    if (child->x < root->x)
    {
        if (root->left == NULL)
        {
            root->left = child;
            return;
        }
        Make_Tree(root->left, child);
    }
    else
    {
        if (root->right == NULL)
        {
            root->right = child;
            return;
        }
        Make_Tree(root->right, child);
    }
}

void preOrder(Tree * root , vector<int> &preorder)
{
    if(root == NULL) return;
    preorder.push_back(root->idx);
    preOrder(root->left, preorder);
    preOrder(root->right, preorder);
}
void postOrder(Tree * root , vector<int> &postorder)
{
    if(root == NULL) return;
    postOrder(root->left, postorder);
    postOrder(root->right, postorder);
    postorder.push_back(root->idx);
}

vector<vector<int>> solution(vector<vector<int>> nodeinfo) {
    vector<vector<int>> answer;
    
    vector<Tree*> trees;
    for (int i = 0; i < nodeinfo.size(); i++)
    {
        Tree *tree = new Tree();
        tree->idx = i+1;
        tree->x = nodeinfo[i][0];
        tree->y = nodeinfo[i][1];
        tree->left = NULL;
        tree->right = NULL;
        
        trees.push_back(tree);        
    }
    sort(trees.begin(), trees.end(), cmp);
    
    Tree *root = trees[0];
    for (int i = 1; i < trees.size(); i++)
    {
        Make_Tree(root, trees[i]);
    }
    
    vector<int> preorder, postorder;
    preOrder(root, preorder);
    postOrder(root, postorder);
    
    answer.push_back(preorder);
    answer.push_back(postorder);
    
    return answer;
}