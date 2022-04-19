#include <iostream>
using namespace std;
int main (){
	char arrchar[10]; 
	
	cout<<"************************************************************"<<endl;
	cout<<"*                                                          *"<<endl;
	cout<<"*              programma che elimina le vocali             *"<<endl;
	cout<<"*                     di un vettore                        *"<<endl;
	cout<<"*                                                          *"<<endl;
	cout<<"************************************************************"<<endl;
	cout<<endl;
	
	for (int i=0; i <10; i++){
		cout <<"inserisci un carattere: ";
		cin>>arrchar [i];
	}
		
	for (int i=0; i <10; i++){
		arrchar [i]=int (arrchar [i]);
		if (arrchar[i]==65 ||arrchar[i]== 97 ||arrchar[i]== 69||arrchar[i]==101||arrchar[i]==73||arrchar[i]==105||arrchar[i]==79||arrchar[i]==111||arrchar[i]==85||arrchar[i]==117){
    		cout<<"";
		}
		else cout <<arrchar [i];
	}
	return 0;
}
