#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define KEYSIZE 16

int main()
{
    int i;
    char key[KEYSIZE];
    
    printf("Current Time: %lld\n", (long long)time(NULL));
    
    //TODO: Comment out this line in Task1.b and record your observations 
    //      What do you think this line does?
    srand(time(NULL)); 
     
    printf("Random Key: ");
    for (i = 0; i < KEYSIZE; i++)
    {
        key[i] = rand() % 256;
        printf("%.2x", (unsigned char)key[i]);
    }
    
    printf("\n");
    
    return 0;
}
