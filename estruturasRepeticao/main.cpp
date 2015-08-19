// custom countdown using while
#include <iostream>
using namespace std;
int main (){
 int n;
 cout << "Entre com um numero> ";
 cin >> n; // pegando o numero da tela

// estrutura while
 while (n>0) {
 cout << n << ", ";
 --n; // decremento
 }
 cout << "Terminou!"; // fim da execução
 return 0;
}