/*Scrivere un programma completo in C++ che, letta in ingresso una 
sequenza di numeri interi su vettore, ne visualizzi il valore masssimo e il minimo*/
#include <iostream>
using namespace std;
int main(){
	
	int len_arr;
	
	cout<<"inserisci il numero di valori:  ";
	cin>>len_arr;
	cout<<"\n";
	len_arr  =  (int const) len_arr;
	
	float arr[len_arr], min, max;
	
	cout<<"inserisci il "<<1<<" numero: ";
	cin>>arr[0];
	max=arr[0];
	min=arr[0];
	
	for (int i=1; i<len_arr; i++){
		cout<<"inserisci il "<<i+1<<" numero: ";
		cin>>arr[i];
		if (arr[i]<min){min=arr[i];}
		if (arr[i]>max){max=arr[i];}
	}
	cout<<"\ni numeri da te inseriti:  ";
	for (int i=0; i<len_arr; i++){
		cout<< arr[i]<<" ";
	}
	cout<<"\nil valore massimo e': "<<max;
	cout<<"\nil valore minimo e': "<<min;
	
fflush (stdin);
getchar();
return 0;
}
