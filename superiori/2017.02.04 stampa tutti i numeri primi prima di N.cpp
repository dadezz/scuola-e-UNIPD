#include <iostream>
using namespace std;

//numero primo?
bool numprimo (int a){
	bool numprimo = true;
	for (int i=2; i<a;i++){
		if (a%i==0){numprimo=false;}
	}
	return numprimo; 
}
//programma principale
int main (){
	int N, sonoprimo, qntNumeriPrimi=0;
	do{
		cout<<"inserisci il tuo numero maggiore di 2: ";
		cin>>N;
	} while (N<=2);
	cout<<"i numeri primi prima di "<<N<<" sono:\n"<<endl;
	for (int i=1; i<=N; i++){
		sonoprimo = numprimo (i);
		if (sonoprimo == true){
			qntNumeriPrimi++;
			cout <<"\t"<<i<<endl;
		}
	}
	cout<<"\ni numeri primi in tutto sono: "<<qntNumeriPrimi<<endl;
	
fflush (stdin);
getchar();
return 0;
}
