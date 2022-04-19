//dati due numeri in input, calcolarne MCD e mcm
#include <iostream>
using namespace std;

int main(){
	int a, b, b1, a1, MCD;
	cout<<"inserisci il primo numero:  ";
	cin>>a;
	cout<<"inserisci il secondo numero:  ";
	cin>>b;
	a1=a;
	b1=b;
	while (a != b) {
			if (b>a){
				int aux=b;
  	 			b=a;	
   				a=aux;
			} 
		a = a-b;
	}
	cout<<"l' MCD tra i due numeri e':   "<<a<<endl;
	cout<<"l'mcm tra i due numeri e':  "<<(a1*b1)/a<<endl;
	fflush (stdin);
	getchar ();
	return 0;
}
