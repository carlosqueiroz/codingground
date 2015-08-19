#include <iostream>

using namespace std;

// função  com retorno
int adicao (int a, int b){ 
 int r; r=a+b; // calculando valores
 return (r); // retorno da função
} 

// função void

void funcao (void){
 cout << "Eu sou uma funcao!";
} 


// inicio main
int main()
{
 int z;
 z = adicao (5,3); // chamando a função e passando parametros
 cout << "O resultado eh " << z; // mostrando resultado
 
 funcao ();  // chamando função void
 return 0; 
}

