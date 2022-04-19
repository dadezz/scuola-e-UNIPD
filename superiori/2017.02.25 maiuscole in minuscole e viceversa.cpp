#include <iostream>
using namespace std;
int main(){
	char lettera;
	do {
		cout<<"inserisci il tuo carattere   ";
		lettera = getchar();
		lettera= int (lettera);
		if (lettera<65 || (lettera>90 && lettera<97) || lettera>122){
			cout<<"questo non e' una lettera\n";
		}
	} while (lettera<65 || (lettera>90 && lettera<97) || lettera>122);
	
	if (lettera>=65 && lettera<=90) {
		cout<<"la lettera e' minuscola.\n";
		lettera = lettera+32;
		lettera = char (lettera);
		cout<<"la corrisondente maiuscola e':  "<<lettera;
	}
	
	if (lettera>=97 && lettera<=122) {
		cout<<"la lettera e' minuscola.\n";
		lettera = lettera-32;
		lettera = char (lettera);
		cout<<"la corrisondente maiuscola e':  "<<lettera;
	}


fflush (stdin);
getchar();
return 0;
}

