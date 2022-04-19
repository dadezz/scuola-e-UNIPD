#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;
int main(){
	int n;
	cout<<"inserisci n:  ";
	cin>>n;
	int arr [n];
	for(int i=0; i<n; i++){
		cout<<"inserisci il valore";
		cin>>arr[i];
	}
	for(int i=0; i<n; i++){
	cout<<arr[i];
	}
fflush (stdin);
getchar();
return 0;
}

