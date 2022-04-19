//orario scolastico
#include <iostream>
#include <string>
using namespace std;
int main(){
string a;
cout<<"inserisci il giorno della settimana (lun, mar, mer, gio, ven, sab, dom)\n";
cin>> a;
while (a!="lun" && a !="mar" && a!="mer" && a!="gio" && a!="ven" && a!="sab" && a!="dom"){
	cout<<"attento! devi inserire un giorno della settimana, nei formati lun, mar, e cosi' via...";
	cout<<"inserisci il giorno della settimana \n";
	cin>> a;
	} 
 	if (a=="lun") {cout<<"ginnastica, ginnastica, scienze, inglese";}
 	else if (a=="mar") {cout<<"fisica, arte, storia, italiano, italiano";}
 	else if (a=="mer") {cout<< "italiano, scienze, scienze, inglese";}
 	else if (a=="gio"){cout<<"storia, inglese, italiano, matematica";}
 	else if (a=="ven") {cout<<"geografia, scienze, matematica, religione, arte";}
 	else if (a=="sab"){cout<<"fisica, matematica, matematica, informatica, informatica";}
 	else {cout<< "sei fortunato! Oggi non c'e' scuola!";}

fflush (stdin);
getchar();
return 0;
}

