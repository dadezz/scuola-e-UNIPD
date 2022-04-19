//in questo programma vado a contare quante volte è presente ogni singola vocale nell'array
#include <iostream>
using namespace std;
int main (){
	cout<<"************************************************************"<<endl;
	cout<<"*                                                          *"<<endl;
	cout<<"*         programma che conta quante volte e'              *"<<endl;
	cout<<"*         presente ogni singola vocale                     *"<<endl;
	cout<<"*                                                          *"<<endl;
	cout<<"************************************************************"<<endl;
	cout<<endl;
	char arrchar[10]; 
	int vocale, a=0, e=0, i=0, o=0, u=0;
	
	for (int cont=0; cont <10; cont++){
		cout <<"inserisci un carattere: ";
		
		cin>>arrchar [cont];
    	arrchar [cont]=int (arrchar [cont]);
		if (arrchar[cont]==65 ||arrchar[cont]== 97 ||arrchar[cont]== 69||arrchar[cont]==101||arrchar[cont]==73||arrchar[cont]==105||arrchar[cont]==79||arrchar[cont]==111||arrchar[cont]==85||arrchar[cont]==117){
			vocale++;
		}
	}
	cout<<"le vocali inserite sono "<<vocale<<", e sono: ";
	
	for (int cont=0; cont <10; cont++){
		if (arrchar[cont]==65 ||arrchar[cont]== 97){
    		a++;
		}
		if (arrchar[cont]== 69||arrchar[cont]==101){
			e++;
		}
		if(arrchar[cont]==73||arrchar[cont]==105){
			i++;
		}
		if (arrchar[cont]==79||arrchar[cont]==111){
			o++;
		}
		if(arrchar[cont]==85||arrchar[cont]==117){
			u++;
		}
	}
	
	cout<<a<<" a, "<<e<<" e, "<<i<<" i, "<<o<<" o, "<<u<<" u.";
		
	return 0;
}
