#include <iostream>
using namespace std;

int main(){
    int num,cont,par;
    par=0;
    cout<<"devi inserire 10 numeri interi"<<endl;
    for (cont=0;cont<10;cont++) {
        cout<<"inserisci il numero";
        cin>>num;
        if(num%2==0){par=par+1;};
    }
    cout<<"i numeri pari sono: "<<par;
fflush (stdin);
getchar ();
return 0;

}

