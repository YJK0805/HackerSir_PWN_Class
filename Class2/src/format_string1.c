#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long long num = 0;
char *flag = "HackerSir{Sup3r_S3cr3t_Fl4g}";
int main(){
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
    char buf[0x20];
    printf("Try to get the flag!");
    scanf("%s", buf);
    printf(buf);
    if(num == 20){
        printf("You got the flag!\n %s", flag);
    }else{
        printf("You failed to get the flag!");
    }
    return 0;
}

