#include<iostream>
#include<climits>

using namespace std;


int main() {

	int T;

	cin >> T;

	int min;
	int mid;
	int max;
	

	for(int i = 0; i < T; i++) {

		int first;
		int second;
		int third;

		cin >> first >> second >> third;

		if(first > second) {
			max = first;
			min = second;
		}
		else{
			max = second;
			min = first;
		}

		if(third > max) {
			mid = max;
			max = third;
		}
		else if(third > min) {
			mid = third;
		}
		else{
			mid = min;
			min = third;
		}

		cout << "Case " << i+1 << ": " << mid << endl;

	}

}