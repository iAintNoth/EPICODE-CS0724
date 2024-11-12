/*Si scriva un programma in linguaggio C che legga due valori interi e visualizzi la loro media aritmetica.*/

#include <stdio.h>


float media(int a, int b){

    float calc = (float)(a + b) / 2;

    return calc;

   
}

int main(){
    int num1;
    int num2;

    printf("Calcoliamo la media di due numeri\n");

    printf("Inserisci un numero: "); 
    scanf("%d", &num1);
    printf("Inserisci un numero:");
    scanf("%d", &num2);

    printf("La media dei due numeri è: %.2f\n", media(num1, num2));



}