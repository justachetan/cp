#include <iostream>
#include <vector>


using namespace std;

int main() {
    
    cout.precision(15);
    int tests;
    cin >> tests;

    for(int i = 0; i < tests; i++) {

        int types;

        cin >> types;
        double total_loss = 0;

        for(int j = 0; j < types; j++) {

            double loss;
            double price;
            double q;
            double d;
        
            cin >> price >> q >> d;

            loss = (price * (d * d) * q)/10000; 
            total_loss = total_loss + loss;
        


        }
        printf("%.10f\n", total_loss);

    }


}
