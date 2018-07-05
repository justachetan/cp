#include<iostream>
#include<cstdio>
#include<cmath>

using namespace std;


int main() {


	float start = 0;
	float first = 0;
	float second = 0;
	float third = 0;

	float total = 0;
	int flag = 0;

	while(true) {

		total = 0;

		scanf("%f %f %f %f", &start, &first, &second, &third);

		if(start == 0 && first == 0 && second == 0 && third == 0) {
			break;
		}

		total = total + 720;

		int diff = first - start;

		if(diff < 0) {

			total = total + ((abs(first - start)/40) * 360);

		}

		else if(diff > 0){

			total = total + 360 - ((abs(first - start)/40) * 360);

		}



		start = first;
		

		total = total + 360;
		

		diff = second - start;

		if(diff < 0) {

			total = total + 360 - ((abs(start - second)/40) * 360);

		}

		else if (diff > 0){

			total = total + ((abs(start - second)/40) * 360);

		}

		start = second;
		

		diff = third - start;

		if(diff < 0) {

			total = total + ((abs(third - start)/40) * 360);

		}

		else if (diff > 0){

			total = total + 360 - ((abs(third - start)/40) * 360);

		}

		start = third;

		printf("%.0f\n", total);

		

	}

	return 0;


}