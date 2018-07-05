#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<vector>
#include<queue>
#include<list>
#include<sstream>
#include<algorithm>

using namespace std;

int min_k(vector<int> input, int hours, int start) {

    if(start == input.size() - 1) {
        return (input[start]/hours) + 1;
    }

    int sub = min_k(input, hours - 1, start + 1);

    if(sub >= input[start]) {
        return sub;
    }
    else {
        return ;
    }
        
}


int main()
{
    int tests;
    cin >> tests;

    for(int i = 0; i< tests; i++) {

        int pile_num;
        int hours;

        cin >> pile_num >> hours;

        vector<int> piles;
        for(int j = 0; j<pile_num; j++){
            
            cin >> piles[j];

        }

        int k = min_k(piles, hours, 0);
        cout << k << endl;

    }
}

