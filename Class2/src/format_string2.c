#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
    char buf[256];
    char *flag = "HackerSir{F0rm4t_Str1ng_1s_3asy}";
    printf("Try to leak the flag!");
    scanf("%s", buf);
    printf(buf, 0xdeadbeef);
    return 0;
}
