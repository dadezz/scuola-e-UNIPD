#include <iostream>
using namespace std;
int main(){
	
	int vett[10], n;
	
	for(int i=0; i<10; i++){
		cout<<"inserisci un numero";
		cin>>vett[i];
	}
	cout<<"scrivi un valore compreso tra 0 e 9";
	cin>>n;
	
	cout<<vett[n];	
	
	
	
	
	
	
	
fflush (stdin);
getchar();
return 0;
}

