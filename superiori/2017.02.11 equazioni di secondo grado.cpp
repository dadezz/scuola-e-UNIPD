#include <iostream>
#include <math.h>
#include <string>
using namespace std;


int main (){
		
	double a, b, c, delta, ris1, ris2; string tipo;
	
	cout<<"tutti i valori da te inseriti dovranno essere quelli della forma \
		semplificata dell'equazione, altrimenti il risultato potrebbe cambiare\n\n";
	cout<<"\tequazione completa = c;"<<endl;
	cout<<"\tequazione spuria   = s;"<<endl;
	cout<<"\tequazione pura     = p;"<<endl;
	
	do {
		cout<<"\n\nora digita la lettera corrispondente   ";
		cin>> tipo;
		if (tipo != "c" && tipo != "s" && tipo != "p") {
			cout<<"carattere non valido\n";
		}
	} while (tipo!= "c" && tipo != "s" && tipo != "p");
	
	if (tipo == "c") {
	
		do {
			cout <<"inserisci il coefficiente della x alla seconda (ovviamente diverso da 0)   ";
			cin>>a;
		} while (a==0);
		do {
			cout <<"inserisci il coefficiente della x (ovviamente diverso da 0)  ";
			cin>> b;
		} while (b==0);
		do {
			cout<<"inserisci il valore noto (ovviamente diverso da 0)   ";
			cin>> c;
		} while (c==0);
		
		delta = (b*b)-(4*a*c);
		if (delta < 0) {
			cout<<"L'equazione risulta impossibile, perchè delta è minore di 0, e in matematica\
				 non ha significato la radice quadrata di un numero negativo";
			fflush (stdin);
			getchar();
            return 0;
		}
		
		ris1 = ((-b)+sqrt(delta))/(2*a);
		ris2 = ((-b)-sqrt(delta))/(2*a);
		
		cout <<"x1 = "<<ris1 <<endl;
		cout <<"x2 = "<<ris2 <<endl;
	}
	
	else if (tipo == "p") {
	
		do {
			cout <<"inserisci il coefficiente della x alla seconda (ovviamente diverso da 0)   ";
			cin>> a;
		} while (a==0);
		do {
			cout<<"inserisci il valore noto (ovviamente diverso da 0)... !!importante!! il valore\
				 noto va inserito come se fosse al 2° membro    ";
			cin>> c;
		} while (c==0);
		if (c==0) {
			cout<<"L'equazione risulta impossibile, perchè il valore noto è minore di 0, e in \
				matematica non ha significato la radice quadrata di un numero negativo";
			return 0;
		}
		
		ris1=(-1)*(sqrt (c));
		ris2=sqrt(c);
		
		cout<<"x1 = "<<ris1<<endl;
		cout<<"x2 = "<<ris2<<endl;
	}
	
	else {	
		
		do {
			cout <<"inserisci il coefficiente della x alla seconda (ovviamente diverso da 0)   ";
			cin>> a;
		} while (a==0);
		do {
			cout <<"inserisci il coefficiente della x (ovviamente diverso da 0)  ";
			cin>> b;
		} while (b==0);
				
		b=-b;
		ris2=b/a;
		
		cout<<"x1 = "<<0<<endl;
		cout<<"x2 = "<<ris2<<endl;		
	}
	

fflush (stdin);
getchar ();
return 0;
}

