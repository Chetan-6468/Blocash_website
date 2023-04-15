#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    // Get current timestamp
    time_t timestamp = time(NULL);
    
    // Generate random number between 0 and 9999
    int rand_num = rand() % 10000;
    
    // Generate transaction ID by concatenating timestamp and random number
    long long transaction_id = timestamp * 10000 + rand_num;
    
    // Print transaction ID
    printf("Transaction ID: %lld\n", transaction_id);
    
    return 0;
}
