//differenza tra il massimo e il minimo di un vettore
#include <iostream>
using namespace std;
int main(){
	int vett[10], max, min, aux;
	for(int i=0; i<10; i++){
		cout<<"inserisci il numero";
		cin>>vett[i];
	}
	max=vett[0];
	min=vett[0];
	for(int i=1; i<10; i++){
		if(vett[i]>max){
			max=vett[i];
		}
		if(vett[i]<min){
			min=vett[i];
		}
	}
	aux=max-min;
	cout<<"la differenza è"<<aux;
	
	fflush (stdin);
	getchar();
return 0;
}

