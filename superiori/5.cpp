//programma che stampa un vettore appena inserito.... xD
#include <iostream>
using namespace std;
int main(){
	
	int n;
	cout<<"scrivi un numero";
	cin>>n;
	int vett[n];
	for(int i=0; i<n; i++){
		cout<<"inserisci un valore";
		cin>>vett[i];
	}
	for(int i=0; i<n; i++){
		cout<<" il numero inserito è"<<vett[i];
	}
	fflush (stdin); 
	getchar ();
	return 0;
}
