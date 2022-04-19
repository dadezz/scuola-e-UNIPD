#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

int first () {
   
   int tipo, peso, galline=0, galli=0, gmagri=0, gnorm=0, gcicc=0;
   srand(time(NULL));

   //da qua in poi faccio la separazione tra galli e galline
   for (int a=0; a<100; a++){
      tipo = rand()%2;       //numero 0 sono le galline, numero 1 i galli
      if (tipo==1) {galli++;}
      else {galline++;}
   ;}


   //da qua in poi faccio la separazione per il peso
   for (int b=0; b<galli; b++){
   peso =rand ()%150;         //ho deciso di mettere come peso massimo 150
   if (peso<60){gmagri++;}
   else if (peso<100){gnorm++;}
   else {gcicc++;}
   ;}
   
   //da qua in poi faccio uscire i risultati
   cout<<"il numero dei pulcini era:  "<<100<<endl;
   cout<<"tra questi il numero delle galline e':  "<<galline<<endl;
   cout<<"mentre il numero di galli e':  "<<galli<<endl;
   cout<<"tra questi ultimi, quelli magri sono:  "<<gmagri<<endl;
   cout<<"quelli normali sono invece:  "<<gnorm<<endl;
   cout<<"infine quelli obesi sono:  "<<gcicc<<endl;

   fflush (stdin);
   getchar ();
   return 0;
}

//ora faccio un secondo programma atto ad occupare meno spazio

int second (){
	
	srand(time(NULL));
   int tipo, peso, galline=0, galli=0, gmagri=0, gnorm=0, gcicc=0;
	
	for (int a=0; a<100; a++){
    	tipo = rand()%4;       //numero 0 sono le galline, numero 1 i galli magri, numero 2 i galli normali, numero 3 quelli obesi 
   		if (tipo==0) {galline++;}
    	else if (tipo==1) {gmagri++;}
    	else if (tipo==2) {gnorm++;}
    	else {gcicc++;}	
   ;}
	
	cout<<"il numero dei pulcini era:  "<<100<<endl;
	cout<<"tra questi il numero delle galline e':  "<<galline<<endl;
   	cout<<"i galli magri sono:  "<<gmagri<<endl;
   	cout<<"i galli normali sono invece:  "<<gnorm<<endl;
   	cout<<"i galli obesi sono:  "<<gcicc<<endl;
	
	fflush (stdin);
	getchar ();
	return 0;
}

