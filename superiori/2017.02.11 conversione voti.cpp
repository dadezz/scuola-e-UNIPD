#include <iostream>
using namespace std;
int main(){
	cout<<"\t**************************************************************"<<endl;
	cout<<"\t*                                                            *"<<endl;
	cout<<"\t*               conversione voti in giudizi                  *"<<endl;
	cout<<"\t*                                                            *"<<endl;
	cout<<"\t**************************************************************"<<endl;
	float voto;
	do {
		cout<<"\ninserire il voto:  ";
		cin>>voto;
		if (voto<0 || voto>10) {
			cout<<"attento, per essere valido il voto deve essere compreso tra 0 e dieci\n";
		}
	} while(voto<0 || voto>10);
	if (voto<=4.5) {cout<<"\ngravemente insufficiente";}
		else if (voto<5.5) {cout<<"\ninsufficiente";}
			else if (voto<6) {cout<<"\nquasi sufficiente";}
				else if (voto<6.75) {cout<<"\nsufficiente";}
					else if (voto<7.75) {cout<<"\ndiscreto";}
						else if (voto<8.75) {cout<<"\nbuono";}
							else if(voto<=9.5) {cout<<"\ndistinto";}
	else {cout<<"ottimo";}
fflush (stdin);
getchar();
return 0;
}

