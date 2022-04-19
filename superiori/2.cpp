//esercizio strano che boh non mi ricordo
#include <iostream>
using namespace std;
int main(){
	int a, aux;
	cout<<"inserisci il numero";
	cin>>a;
	if(a<4){
		aux=a-(20*a/100);
		cout<<"il prezzo finale è"<<aux;
	}
	else if(a<8){
		aux=a-(50*a/100);
		cout<<"il prezzo finale è"<<aux;
	}
	else{
		aux=a-(80*a/100);
		cout<<"il prezzo finale è"<<aux;
	}
	
	
	
fflush (stdin);
getchar();
return 0;
}

