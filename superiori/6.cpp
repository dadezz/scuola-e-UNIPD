//programma che legge un vettore al contrario
#include <iostream>
using namespace std;
int main(){
	
	int n;
	cout<<"inserisci un numero";
	cin>>n;
	int vett[n];
	for(int i=0; i<n; i++){
		cout<<"inserisci un valore";
		cin>>vett[i];
	}
	for(int i=n-1; i>=0; i--){
		cout<<"il numero è"<<vett[i];
		}
fflush (stdin);
getchar();
return 0;
}

