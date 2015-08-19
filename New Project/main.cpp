#include <iostream>

using namespace std;
// variaveis globais
 int a,b,c;
 int soma;


int main()
{
    // Variaveis Locais
    std::string nome; // declarando string
    
    // Definindo Constantes # não é instrução, portanto não necessita ;
   
    #define PI 3.14159265  
    #define NEWLINE '\n'
    const int largura = 100; 
    
    
    // Contexto do programa
    a=2;
    b=5;
    c=3;
    soma=a+b+c;
    nome ="nome escrito";

    // mostrando na tela
   cout << nome<< endl; 
   
   // terminando o programa
   return 0;
}

