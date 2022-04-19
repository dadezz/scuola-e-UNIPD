#include <iostream>
using namespace std;
int main (){
	char arrchar[10]; 
	int vocale;
	cout<<"************************************************************"<<endl;
	cout<<"*                                                          *"<<endl;
	cout<<"*         programma che conta il numero di vocali          *"<<endl;
	cout<<"*               di un vettore e le stampa.                 *"<<endl;
	cout<<"*                                                          *"<<endl;
	cout<<"************************************************************"<<endl;
	cout<<endl;
	
	for (int i=0; i <10; i++){
		cout <<"inserisci un carattere: ";
		
		cin>>arrchar [i];
    	arrchar [i]=int (arrchar [i]);
		if (arrchar[i]==65 ||arrchar[i]== 97 ||arrchar[i]== 69||arrchar[i]==101||arrchar[i]==73||arrchar[i]==105||arrchar[i]==79||arrchar[i]==111||arrchar[i]==85||arrchar[i]==117){
			vocale++;
		}
	}
	cout<<"le vocali inserite sono "<<vocale<<", e sono: ";
	
	for (int i=0; i <10; i++){
		if (arrchar[i]==65 ||arrchar[i]== 97 ||arrchar[i]== 69||arrchar[i]==101||arrchar[i]==73||arrchar[i]==105||arrchar[i]==79||arrchar[i]==111||arrchar[i]==85||arrchar[i]==117){
    		cout <<arrchar [i]<<", ";
		}
	}
	return 0;
}

