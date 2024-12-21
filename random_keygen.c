#include <stdio.h>
#include <stdlib.h>
#define LEN 32 // TODO: Modify to generate a 256-bit encryption key note this length is in bytes

int main()
{
    
    unsigned char *key = (unsigned char *)malloc(sizeof(unsigned char) * LEN);
    //TODO: provide the name of the file passes as an input argument 
    // (that is the source of randomness), to fopen 
    FILE *random = fopen("output.bin", "r");
    fread(key, sizeof(unsigned char) * LEN, 1, random);
    fclose(random);
    
    /* TODO: print the key to the terminal as follows:
     * You can use a for loop like the one in 
     * random_time.c to print out the key
     */
    for (int i = 0; i < LEN; i++) {
        printf("%.2x", key[i]);
    }
    
    printf("\n");
    return 0;
}
