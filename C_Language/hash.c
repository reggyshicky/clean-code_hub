# define CAPACITY 50000 /*size of the hash table*/

unsigned long hash_function(char *str)
{
    unsigned long int i = 0;
    int j;

    for (j = 0; str[j]; j++)
    {
        i = i + str[j];
    }
    return i % CAPACITY; 

}