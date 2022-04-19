//inversione valori
#include <iostream>
using namespace std;
int main () {
    int primonumero, secondonumero, aux;
    cout<<"inserisci il primo numero:  ";
    cin>>primonumero;
    cout <<"inserisci il secondo numero: ";
    cin>>secondonumero;
    aux=secondonumero;
    secondonumero=primonumero;
    primonumero=aux;
    
    cout <<"numero1= "<< primonumero; 
	cout<<"     numero2= " << secondonumero;
    
    fflush (stdin);
getchar ();
return 0;
    }
