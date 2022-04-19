#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main (){
   int t, mm=0, mg=0, mr=0, mv=0;
   srand(time (NULL));
   for (int a=0; a<200; a++){
      t=rand ()% 4;
      switch (t) {
         case 1: mr++;
                 break;
         case 2: mg++;    
                 break; 
         case 3: mv++;
                 break;
         default: mm++;
      }
   ;}
cout<<"le mele marce sono:  "<<mm<<endl;
cout<<"le mele gialle sono:  "<<mg<<endl;
cout<<"le mele verdi sono:  "<<mv<<endl;
cout<<"le mele rosse sono:  "<<mr<<endl;

fflush (stdin);
getchar ();
return 0;
}

