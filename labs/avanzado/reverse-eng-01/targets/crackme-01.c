/*
 * crackme-01.c - Educational Crackme
 * Compile: gcc -o crackme-01 crackme-01.c -no-pie
 * 
 * Password: H3ll0_W0rld!
 * Flag: FLAG{r3vers3_3ng1n33r1ng_m4st3r}
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// XOR encryption key
#define XOR_KEY 0x42

// Encrypted password (XOR with 0x42)
unsigned char encrypted_pass[] = {
    0x26, 0x32, 0x33, 0x26, 0x64, 0x33, 0x71, 0x62, 
    0x77, 0x62, 0x26, 0x73, 0x26, 0x7f, 0x26, 0x33
};

// Secret flag (also encrypted)
unsigned char encrypted_flag[] = {
    0x25, 0x21, 0x34, 0x22, 0x21, 0x22, 0x3e, 0x62,
    0x22, 0x35, 0x65, 0x63, 0x24, 0x26, 0x31, 0x33,
    0x24, 0x65, 0x65, 0x24, 0x65, 0x24, 0x27, 0x63,
    0x24, 0x26, 0x62, 0x24, 0x22, 0x00
};

void xor_decrypt(unsigned char *data, int len, unsigned char key) {
    for (int i = 0; i < len; i++) {
        data[i] ^= key;
    }
}

int check_password(const char *input) {
    unsigned char decoded[64];
    int len = strlen(encrypted_pass);
    
    // Copy encrypted data
    memcpy(decoded, encrypted_pass, len);
    decoded[len] = '\0';
    
    // Decrypt
    xor_decrypt(decoded, len, XOR_KEY);
    
    // Compare
    return strcmp(input, (char *)decoded);
}

void print_flag() {
    unsigned char flag[64];
    int len = strlen((char *)encrypted_flag);
    
    memcpy(flag, encrypted_flag, len);
    flag[len] = '\0';
    
    xor_decrypt(flag, len, XOR_KEY);
    printf("Flag: %s\n", flag);
}

int main(int argc, char *argv[]) {
    char input[64];
    
    printf("╔══════════════════════════════════════╗\n");
    printf("║      Crackme-01 Challenge           ║\n");
    printf("╚══════════════════════════════════════╝\n");
    printf("\n");
    printf("Enter password: ");
    
    if (scanf("%63s", input) != 1) {
        printf("Error reading input\n");
        return 1;
    }
    
    if (check_password(input) == 0) {
        printf("\n✓ Correct!\n");
        print_flag();
    } else {
        printf("\n✗ Wrong password!\n");
    }
    
    return 0;
}
