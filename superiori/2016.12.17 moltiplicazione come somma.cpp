#include <iostream>
using namespace std;


int main (){
	int fattore1, fattore2, risultato =0, contatore =0;
	cout <<"inserisci il primo fattore:  ";
	cin>> fattore1;
	cout <<"inserisci il secondo fattore:  ";
	cin>> fattore2;
	if (fattore1==0 || fattore2==0) {
		cout<<0;
		return 0;
	}
	else if (fattore1> 0 && fattore2>0) {
		for (int contatore =0; contatore <fattore2; contatore++) {
		risultato= risultato+fattore1;
		};
	}
	else {
		for (contatore=0; contatore > fattore2 || contatore>fattore1;contatore --)
		{risultato=risultato-fattore1;
		};
	}
	cout<<risultato <<endl;
	fflush (stdin);
	getchar ();
	return 0;
}
