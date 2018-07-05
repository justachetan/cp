#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main(){

	//char * out = new char[100];
	string out("");
	out[0] = '\0';
	char inp;
	int i = 0;
	int flag = 0;

	while(true){


		cin >> inp;



		if(inp == EOF){
			break;
		}

		if(inp != '\"') {

			out+=inp;
		}

		else if(flag == 0) {

			out+="``";
			flag = 1;

		}

		else if(flag == 1) {

			out+="''";

			// out[i] = '\'';
			// out[i+1] = '\'';
			// out[i+2] = '\0';
			i = i+2;
			flag = 0;

		}


		

	}

	cout << out << endl;


}