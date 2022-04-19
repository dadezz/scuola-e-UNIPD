#include <iostream>
using namespace std;
int main(){
	
	cout<<"************************************************************"<<endl;
	cout<<"*                                                          *"<<endl;
	cout<<"*         programma che controlla se un certo              *"<<endl;
	cout<<"*           carattere sia o meno presente                  *"<<endl;
	cout<<"*                   nel vettore                            *"<<endl;
	cout<<"*                                                          *"<<endl;
	cout<<"************************************************************"<<endl;
	cout<<endl; 
	
	int n, i;
	bool c=false;
	char vett[n], x;
	
	cout<<"inserisci il numero di caratteri di cui e' formato il vettore: ";
	cin>>n;
	cout<<"inserisci il carattere che vuoi controllare: ";
	cin>>x;	
	cout<<"\n";

	for (i=0; i<n; i++){
		cout<<"inserisci un carattere: ";
		cin>>vett[i];
	}
	
	for (i=0; i<n; i++){
		if (vett[i]==x){
			c=true;
		}
	}
	
	if (c){cout<<"evviva e' presente!";}
		else{cout<<"spiacenti, non e' stato trovato";}
	fflush (stdin);
	getchar();
	return 0;
}

