#include <iostream>
using namespace std;
int main(){
int giorno, mese, maxgiorno;
cout<<"\n\n\t\t\t\tSEGNO ZODIACALE\n\n";
cout<<"per inserire un mese devi usare un numero\n\n";
cout<<"\tgennaio = 1\n";
cout<<"\tfebbraio = 2 \n";
cout<<"\tmarzo = 3\n";
cout<<"\taprile = 4 \n";
cout<<"\tmaggio = 5 \n";
cout<<"\tgiugno = 6 \n";
cout<<"\tluglio = 7 \n";
cout<<"\tagosto = 8\n";
cout<<"\tsettembre = 9 \n";
cout<<"\tottobre = 10 \n";
cout<<"\tnovembre = 11 \n";
cout<<"\tdicembre = 12 \n\n";
cout<<"ora che sai che numeri inserire, inserisci il numero:    ";
cin>>mese;
if (mese < 1 || mese > 12) {
	cout<<"\nil programma non puo' essere eseguito perche' devi inserire un mese valido"; 
	getchar();
	return 0;}
if (mese == 2) {maxgiorno=29;}
else if (mese == 4 || mese == 6 || mese == 9 || mese == 11) {maxgiorno = 30;}
else {maxgiorno=31;}		
cout<<"\nora devi inserire il tuo giorno di nascita (il numero):   ";
cin>>giorno;
if (giorno<1) {
	cout<<"\nil programma non puo' essere eseguito perche' devi inserire un giorno valido"; 
	getchar();
	return 0;
}
if (giorno > maxgiorno) {
	cout<<"\nil programma non puo' essere eseguito perche' devi inserire un giorno valido";
	getchar ();
	return 0;
}
else {	
	switch (mese){
		case (1):
			if (giorno<21) {cout<<"\nsei del segno del capricorno";}
 			else {cout<<"\nsei del segno dell'acquario";}
 			break;
 		case (2):
 			if (giorno<20) {cout<<"\nsei del segno dell'acquario";}
 			else {cout<<"\nsei del segno dei pesci";}
 			break;
 		case (3):
 			if (giorno<21) {cout<<"\nsei del segno dei pesci";}
 			else {cout<<"\nsei del segno dell'ariete";}
 			break;
 		case (4):
 			if (giorno<21) {cout<<"\nsei del segno dell'ariete";}
 			else {cout<<"\nsei del segno del toro";}
 			break;
 		case (5):
 			if (giorno<21) {cout<<"\nsei del segno del toro";}
 			else {cout<<"\nsei del segno dei gemelli";}
 			break;
 		case (6):
 			if (giorno<22) {cout<<"\nsei del segno dei gemelli";}
 			else {cout<<"\nsei del segno del cancro";}
 			break;
 		case (7):
 			if (giorno<23) {cout<<"\nsei del segno del cancro";}
 			else {cout<<"\nsei del segno del leone";}
 			break;
 		case (8):
 			if (giorno<24) {cout<<"\nsei del segno del leone";}
 			else {cout<<"\nsei del segno della vergine";}
 			break;
 		case (9):
 			if (giorno<23) {cout<<"\nsei del segno della vergine";}
 			else {cout<<"\nsei del segno della bilancia";}
 			break;
 		case (10):
 			if (giorno<23) {cout<<"\nsei del segno della bilancia";}
 			else {cout<<"\nsei del segno dello scorpione";}
 			break;
 		case (11):
 			if (giorno<22) {cout<<"\nsei del segno dello scorpione";}
 			else {cout<<"\nsei del segno del saggittario";}
 			break;
 		case (12):
 			if (giorno<22) {cout<<"\nsei del segno del saggittario";}
 			else {cout<<"\nsei del segno del capricorno";}
 			break;
	}
} 
fflush (stdin);
getchar();
return 0;
}
