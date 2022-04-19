#include <iostream>
using namespace std;
int main(){
	
	int vett[10], aux=0;
	
	for(int i=0; i<10; i++){
		cout<<"inserisci un numero";
		cin>>vett[i];
	}
	for(int i=0; i<10; i++){ 
	if (vett[i]%2==0){
		aux++;
	}
	}
	cout<<"i numeri pari sono"<<aux;
	
	
	
fflush (stdin);
getchar();
return 0;
}

