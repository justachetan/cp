#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<vector>
#include<queue>
#include<list>
#include<sstream>
#include<algorithm>

using namespace std;

typedef long long ll;

int main()
{
   int tests;

   cin >> tests;

   for(int i = 0; i < tests; i++)
   {
        string inp;
        int num;

        cin >> inp >> num;
        string tmp = inp;
        /*
        for(int j = 1; j< num;j++){

            inp.append(tmp);

        }
        */

        int count_a = 0;
        int count_b = 0;
        int prefix = 0;

        for (int i = 0; i < num; i++){
            for(int j = 0; j < inp.length();j++) {

                if(inp[j] == 'a'){
                
                    count_a++;

                }
                else {

                    count_b++;

                }

                if(count_a > count_b) {

                    prefix++;

                }

            }
        }
        cout << prefix <<endl;


   }

}

