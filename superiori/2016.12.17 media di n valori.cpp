#include <iostream>
using namespace std;

int main (){
	float numero1, numero2;
	int n, contatore; 
	numero2=0;
	cout<<"inserisci il numero di valori di cui si vuole fare la media:  ";
	cin>>n;
	if (n==0 || n<0 || n==1) { 
		cout<<"inserire un numero diverso da che sia maggiore di 1...    "<<endl;
		cout<<"inserisci il numero di valori di cui si vuole fare la media:  ";
		cin>>n;
	} 
 for (contatore=0; contatore<n; contatore++)
		{ cout<<"inserisci il valore   ";
		cin>>numero1;
		numero2 = numero2+numero1;
		}
	float risultato=numero2/n;
	cout<<risultato;
	
	fflush (stdin);
	getchar ();
	return 0;
}
	
	
