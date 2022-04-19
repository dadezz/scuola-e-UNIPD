#include <iostream>
using namespace std;
int main () {

int numero1;
    cout <<"inserire il primo numero:  ";
    cin>> numero1;
if (numero1 < 0) {numero1=-numero1;}
cout << numero1;
    
fflush (stdin);
getchar ();
return 0;
}
