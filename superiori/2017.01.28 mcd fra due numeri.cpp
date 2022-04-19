/*per calcolare l'mcd ho deciso di utilizzare il metodo di euclide, che è meglio del metodo classico per due motivi: 
1: perchè permette di utilizzare solo le variabili contenenti i due numeri, così da occupare meno spazio;
2: perchè permette di avere un tempo di risoluzione minore
*/
#include <iostream>
using namespace std;
int main(){
	int a, b;
	cout<<"inserisci il primo numero:  ";
	cin>>a;
	cout<<"inserisci il secondo numero:  ";
	cin>>b;
	
	while (a != b) {
		if (b>a){
			int aux=b;
    		b=a;
    		a=aux;
		} 
		a = a-b;
	}
	
	cout<< "l'mcd tra i due numeri risulta essere "<<a;
fflush (stdin);
getchar();
return 0;
}

