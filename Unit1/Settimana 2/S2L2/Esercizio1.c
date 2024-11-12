/*Si scriva un programma che esegua l'operazione di moltiplicazione tra due numeri inseriti dall'utente.*/

#include <stdio.h>


int main(){
    int num1;
    int num2;
    int prodotto;


    printf("Calcoliamo la moltioplicazione tra numeri\n");

    printf("Inserisci un numero: ");
    scanf("%d", &num1);
    printf("Inserisci un numero: ");
    scanf("%d", &num2);

    prodotto = num1 * num2;

    printf("Il prodotto dei due numeri e': %d", prodotto);
}