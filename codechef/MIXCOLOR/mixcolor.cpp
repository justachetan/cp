#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<vector>
#include<queue>
#include<list>
#include<sstream>
#include<algorithm>

using namespace std;


int main()
{
    
    int tests;
    cin >> tests;

    for(int i = 0;i < tests; i++) {

        vector<int> present;

        int size;
        cin >> size;
        int changes = 0;
        for(int j = 0; j< size; j++) {

            int next;
            cin >> next;

            present.push_back(next);

         }

        sort(present.begin(), present.begin() + size);

        for(int j = 1; j < size; j++) {
            
            if(present[j] == present[j - 1]) {
                changes++;
            }

        }
        cout << changes << endl;

    }

}

