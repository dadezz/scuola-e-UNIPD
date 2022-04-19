#include <iostream>
#include <stdlib.h>
using namespace std;
int main(){

	  int vett[10];
	  
	  for(int i=0; i<10; i++){
	  	vett[i]=rand()%1000;	
	  }
	  for(int i=0; i<10; i++){
	  if(vett[i]<250){
	  	cout<<1;
	  }
	  else if(vett[i]<500){
	  	cout<<2;
	  }
	  else {
	  	cout<<3;
	  }
	  }
	
	
fflush (stdin);
getchar();
return 0;
}

