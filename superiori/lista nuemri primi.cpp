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
	int sonoprimo;
	int i=1;
	do{	sonoprimo = numprimo (i);
		if (sonoprimo == true){
			cout <<"\t"<<i<<endl;
		}
		i++;
	}while (i>0);

fflush (stdin);
getchar();
return 0;
}
