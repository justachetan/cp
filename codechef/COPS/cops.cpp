#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main(){

		int T;

		cin >> T;

		for(int i=0; i< T; i++) {

				int M, x, y;

				cin >> M >> x >> y;
				
				int arr[M];
				int ans = 100;

				for (int j=0; j < M; j++) {

						cin >> arr[i]
				}
				
				sort(arr, arr+M);
				
				for(int j =0; j < M; j++) {

						front_cover = arr[i] + x*y;
						if(front_cover > 100) {
								front_cover = 100;
						}
						back_cover = arr[i] - x*y;
						if(back_cover < 1) {
								back_cover = 1;
						}
						
				}

		}

		

}
