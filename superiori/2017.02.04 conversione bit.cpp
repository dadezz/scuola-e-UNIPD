//conversione binario-decimale
#include <iostream>
#include <cmath>
using namespace std;
int main(){
	
	int n, bit, somma, exp, pot;
	cout<<"inserisci il numero di bit che si volgiono inserire:  ";
	cin>>n;
	somma = 0;
	exp=n-1;
	
	for (int i=0; i<n; i++){
		do {
			cout<<"inserisci il bit";
			cin>>bit;
		} while (bit != 1 && bit!=0);
		pot= bit*pow(2,exp);
		somma=somma+pot;
		exp--;
	}
	
	cout<<somma;

fflush (stdin);
getchar();
return 0;
}

