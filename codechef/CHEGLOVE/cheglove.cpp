#include <iostream>
#include <vector>
using namespace std;


int main() {

    int tests;

    cin >> tests;

    for(int i = 0; i < tests; i ++) {

        vector<int> glove;
        vector<int> hand;
        vector<int> reverse;
        bool front = true;
        bool back = true;
        int size;

        cin >> size;

        for(int j = 0; j < size; j++) {

            int finger;
            cin >> finger;
            hand.push_back(finger);

        }
        
        for(int j = 0; j< size; j++) {

            int sheath;
            cin >> sheath;
            if(sheath < hand[j]) {
                front = false;
            }
            if(sheath < hand[size - j - 1]){
                back = false;
            }
            glove.push_back(sheath);

        }



        if(front && back) {
            cout << "both" <<endl;
        }
        else if(front) {
            cout << "front" <<endl;

        }
        else if(back) {
            cout << "back" << endl;
        }
        else {
            cout << "none" <<endl;
        }
    



    }


}
