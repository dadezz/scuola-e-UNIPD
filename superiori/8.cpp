//media aritmetica di 10 valori
#include <iostream>
using namespace std;
int main(){
	
	int vett[10], mediaaritmetica, somma;
	
	somma=0;
	for(int i=0; i<10; i++){
		cout<<"inserisci il valore";
		cin>>vett[i];
		somma=somma+vett[i];	
	}
    mediaaritmetica=somma/10;
	cout<<"la media aritmetica è"<<mediaaritmetica;	
	
	
fflush (stdin);
getchar();
return 0;
}

