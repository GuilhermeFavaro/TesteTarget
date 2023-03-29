#include <stdio.h>
#include <string.h>

char inverte_string(char vetor[]){
    char vetor_invertido[10], *p;
    int x, tam = 0;

    tam = strlen(vetor);
    p = vetor + tam - 2;

    for(x = 0; x < tam; x++){
        vetor_invertido[x] = *p;
        p--;
    }

    for(x = 0; x < tam; x++){
        printf("%c", vetor_invertido[x]);
    }

}

int main(){
    char vetor[10];

    fgets(vetor, 10, stdin);

    inverte_string(vetor);
}