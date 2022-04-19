#include <iostream>
using namespace std;
int main(){
	
	cout<<"************************************************************"<<endl;
	cout<<"*                                                          *"<<endl;
	cout<<"*         programma che conta quante volte un certo        *"<<endl;
	cout<<"*           carattere sia presente nel vettore             *"<<endl;
	cout<<"*                                                          *"<<endl;
	cout<<"************************************************************"<<endl;
	cout<<endl; 
	
	int n, i, numero_di_volte=0;
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
			numero_di_volte++;
		}
	}
	
	if (c==true){cout<<"evviva e' presente, "<<numero_di_volte<<" volte.";}
		else{cout<<"spiacenti, non e' stato trovato";}
	fflush (stdin);
	getchar();
	return 0;
}
