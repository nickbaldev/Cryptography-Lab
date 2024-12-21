#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define KEYSIZE 16

int main()
{
    int i;
    char key[KEYSIZE];
    time_t t;
    /*TODO: Currently the variable t is not initialized. 
            using a loop, set t to generate seeds within a two hour 
            window before the timestamp associated with Alice's encrypted 
            file.
     */

    for (t=1524013729; t<1524020930; t++)
    {

   	 srand(t);
   	 for (i = 0; i < KEYSIZE; i++)
   	 {
       		 key[i] = rand() % 256;
       		 printf("%.2x", (unsigned char)key[i]);
  	 }
   	 printf("\n");
    }

    return 0;
}
