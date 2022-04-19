/*
programma che, data una lettera in input,
la stampa  a video in maiuscolo e in minuscolo.
Sono usati: 
-type-casting da intero a carettere
-le funzioni toupper e to lower
*/
#include <iostream>
using namespace std;

int main(){

	char a, A;									//inizializzo la mia variabile
	cout<<"inserisci il tuo carattere: ";
	a=getchar();								//la ricevo in input
	a= (char)toupper (a);						//la faccio diventare maiuscola
	cout<<"\nla lettera in maiuscolo e': "<<a;	//stampo la lettera in maiuscolo
	a= (char)tolower (a);						//la faccio diventare minuscola
	cout<<"\nla lettera in minuscolo e': "<<a;	//stampo la lettera in minuscola

fflush (stdin);
getchar();
return 0;
}

