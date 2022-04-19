#include <iostream>
using namespace std;
int main () {
    int num, max, min, contatore, n;
    cout <<"inserire il numero di valori tra cui si vuole trovare il massimo e il minimo:  ";
    cin>>n;  
    	if (n<1) {
    	cout <<"n deve essere diverso da 0 e da 1\n";
    }
    cout <<"inserisci il primo dei valori";
    cin>>num;
    max=num;
    min=num;    
	for (contatore =1; contatore<n; contatore++)
		{cout<<"inserisci un altro valore: ";
		 cin>>num;
			if (num<min) {min=num;}
			if (num>max) {max=num;}
	}	
	cout<< "il minimo tra i numeri e': "<<min<<endl;
	cout<< "il massimo tra i numeri e': "<<max;
	fflush (stdin);
getchar();
return 0;
}
    
