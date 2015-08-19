#include <iostream>
/*
É possível declarar variáveis locais e globais com o mesmo
nome dentro de um bloco. Para acessar uma variável global
quando uma variával local com o mesmo nome está no escopo,
usa-se o operador :: (resolução de escopo).
*/
using namespace std;
int ref = 1000; // variavel global

// funcoes
int quadrado(int x){
 return x * x;
}
double quadrado (double y){
 return y * y;
} 


int main()
{
   int j = 0;
 if (j == 0)
 {
 int ref = 2; // variavel local
 cout << ref*::ref << endl; // calculando variavel local com global de mesmo nome usando ::
 }
 
 // sobrecarga de funcoes
 int r1; double f1;
 r1 = quadrado( 7 );
 f1 = quadrado ( 2.2 );
 cout << “r1 = ” << r1 << “, f1 = ” << f1 << endl; 
 
 
   
   return 0;
}

