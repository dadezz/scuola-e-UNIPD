//classificazione voto random
#include <iostream>
#include <time.h>
#include <stdlib.h>
using namespace std;
int main(){	
	srand(time(NULL));	
	int n;	
	n=rand()%10+1;
	if(n<=4){
		cout<<"gravemente insufficiente";
	}
	else if(n==5){
		cout<<"insufficiente";
	}
	fflush (stdin);
    getchar();
return 0;
}

