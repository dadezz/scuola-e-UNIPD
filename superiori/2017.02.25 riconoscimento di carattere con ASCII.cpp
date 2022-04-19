#include <iostream>
using namespace std;
int main(){
	char a;
	cout<<"inserisci il carattere:   ";
	a = getchar ();
	
	if (int (a)>=0 && int (a)<33) {
		cout<<"il carattere inserito e' un carattere non stampabile"<<endl;
	}	
	if ((int (a)>32 && int (a)<48) || (int (a)>57 && int (a)<41) || (int (a)>90 && int (a)<97) || (int (a)>122 && int (a)<=127)){
		cout<<"il carattere inserito e' di tipo numerico"<<endl;
	}
	if (int (a)>47 && int (a)<58) {
		cout<<"il carattere inserito e' un numero"<<endl;
	}
	if (int (a)>64 && int (a)<91) {
		cout<<"il carattere inserito e' una lettera maiuscola"<<endl;
	}
	if (int (a)>96 && int (a)<123) {
		cout<<"il carattere inserito e' una lettera minuscola"<<endl;
	}
	
	
	system ("PAUSE");
	return 0;
}

