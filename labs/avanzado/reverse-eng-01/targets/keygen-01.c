/*
 * keygen-01.c - Educational Keygen Challenge
 * Compile: gcc -o keygen-01 keygen-01.c -no-pie -lcrypto
 * 
 * Serial Algorithm: MD5(username + "CDPN_SALT")[:8]
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <openssl/md5.h>

#define SALT "CDPN_SALT"

void compute_serial(const char *username, char *serial) {
    char buffer[256];
    unsigned char hash[MD5_DIGEST_LENGTH];
    
    // Concatenate username + salt
    snprintf(buffer, sizeof(buffer), "%s%s", username, SALT);
    
    // Compute MD5
    MD5((unsigned char*)buffer, strlen(buffer), hash);
    
    // Take first 8 hex chars
    for (int i = 0; i < 8; i++) {
        sprintf(&serial[i*2], "%02x", hash[i]);
    }
    serial[16] = '\0';
}

int verify_serial(const char *username, const char *serial) {
    char expected[32];
    compute_serial(username, expected);
    return strcmp(serial, expected) == 0;
}

int main(int argc, char *argv[]) {
    char username[128];
    char serial[32];
    char input_serial[32];
    
    printf("╔══════════════════════════════════════╗\n");
    printf("║      Keygen-01 Challenge            ║\n");
    printf("╚══════════════════════════════════════╝\n\n");
    
    printf("Enter username: ");
    if (scanf("%127s", username) != 1) {
        printf("Error reading username\n");
        return 1;
    }
    
    compute_serial(username, serial);
    
    printf("\nGenerated serial: %s\n\n", serial);
    
    // Verify
    printf("Enter serial to verify: ");
    if (scanf("%31s", input_serial) != 1) {
        printf("Error reading serial\n");
        return 1;
    }
    
    if (verify_serial(username, input_serial)) {
        printf("\n✓ Valid serial!\n");
        printf("Flag: FLAG{k3yg3n_m4st3r_%s}\n", username);
    } else {
        printf("\n✗ Invalid serial!\n");
    }
    
    return 0;
}
