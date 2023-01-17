#include <stdio.h>

int main() {
  char ch[250]={0};
  char a[250] ={0};
  int h;
  int i,j,k,l,n,m;


  while(1){
    i=0;
    while(1){
      
      scanf("%c",&ch[i]);
      if(ch[i] == '\n') {    
	break;
      }
      
      i++;
    }
   
    if ( i == 1 && ch[0] == '-' ) break;

    //  printf("%d",i);
    
    scanf("%d",&m);
    
    for(j=0;j<m;j++){
      scanf("%d", &h );
      
      for(k=0;k<i-h;k++) {
	a[k] = ch[h+k];
	//    printf("a[%d] = ch[%d]の%c\n",k ,h+k,ch[h+k]);
      }
      for(k=0;k<h;k++){
	a[i-h+k] = ch[k];
	//   printf("a[%d] = ch[%d]の%c\n",i-h+k,k,ch[k]);
      }
      for(k=0; k<i; k++){
	ch[k] = a[k];
	// printf("ch[%d] = a[%d]の%c\n",k,k,a[k]);
      }
    }
    for(k=0;k<i;k++) {
      printf("%c",ch[k]);
    }
    printf("\n");
      scanf("%c",&ch[0]);
  }
  
  
  return 0;
  
}
