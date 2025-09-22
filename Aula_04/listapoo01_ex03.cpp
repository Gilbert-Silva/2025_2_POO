#include <iostream>

using namespace std;

class Conta {
    public:
    string titular;  // Declaração dos atributos
    string numero;
    double saldo;
    Conta() {                      // Construtor
        titular = "sem nome";      // Atributos
        numero = "sem número";
        saldo = 0;
    }
    void depositar(double valor) {
        saldo += valor;
    }    
    void sacar(double valor) {
        saldo -= valor;
    }
};

int main() {
    Conta x;                // x é uma instância
    Conta& y = x;           // y é uma referência para x
    Conta* z = new Conta(); // z é um ponteiro para a instância
    cout << x.titular << " " << x.numero << " " << x.saldo << endl;
    x.titular = "Raquel";
    x.numero = "123-x";
    x.saldo = 1000;
    cout << x.titular << " " << x.numero << " " << x.saldo << endl;
    x.depositar(500);
    cout << x.titular << " " << x.numero << " " << x.saldo << endl;
    y.depositar(1000);
    cout << x.titular << " " << x.numero << " " << x.saldo << endl;
    z->numero = "123";
    (*z).numero = "456";
    delete z;
    return 0;
}


