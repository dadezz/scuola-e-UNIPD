/*Scrivere un programma completo in C++ che, letta in ingresso una 
sequenza di numeri interi su vettore, 
ne visualizzi la sequenza e restituisca la media aritmetica.
*/
#include <iostream>
using namespace std;
int main(){
	
	int len_arr;
	cout<<"inserisci il numero di valori di cui si vuole fare la media:  ";
	cin>>len_arr;
	cout<<"\n";
	len_arr  =  (int const) len_arr;
	float arr[len_arr];
	for (int i=0; i<len_arr; i++){
		cout<<"inserisci il "<<i+1<<" numero: ";
		cin>>arr[i];
	}
	cout<<"\ni numeri da te inseriti:  ";
	for (int i=0; i<len_arr; i++){
		cout<< arr[i]<<" ";
	}
	for (int i=1; i<len_arr; i++){
		arr[0]+= arr[i];
	}
	arr[0]= arr[0]/len_arr;
	cout<<"\n\nla media di tutti i numeri e': "<<arr [0];
	
fflush (stdin);
getchar();
return 0;
}
