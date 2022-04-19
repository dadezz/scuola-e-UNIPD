//media, somma, prodotto
#include<iostream>
using namespace std;

int main(){
	 int a, b, c, aux, aux2, aux3, aux4;
	 cout<<"scrivi il primo numero";
	 cin>>a;
	 cout<<"scrivi il secondo numero";
	 cin>>b;
	 cout<<"scrivi il terzo numero";
	 cin>>c;
	 cout<<"per fare la media aritmetica scrivi 1, per la somma 2 e per il prodotto 3";
	 cin>>aux;
	 if(aux==1){
	 	aux2=(a+b+c)/3;
	 	cout<<"la media aritmetica è"<<aux2;
	 }
	 if(aux==2){
	 	aux3=a+b+c;
	 	cout<<"la somma è"<<aux3;
	 }
	 if(aux==3){
	 	aux4=a*b*c;
	 	cout<<"il prodotto è"<<aux4;
	 }
	 
	fflush(stdin);
	getchar();
	return 0;
}
