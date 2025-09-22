class Conta {
    public String titular;                // Declaração dos atributos
    public String numero;
    public double saldo;
    public Conta() {                      // Construtor
        titular = "sem nome";             // Atributos
        numero = "sem número";
        saldo = 0;
    }
    public void depositar(double valor) {
        saldo += valor;
    }    
    public void sacar(double valor) {
        saldo -= valor;
    }
}

public class listapoo01_ex03 {
    public static void main(String[] args) {
        Conta x = new Conta();    // x é uma referência
        System.out.println(x.titular + " " + x.numero + " " + x.saldo);
        x.titular = "Raquel";
        x.numero = "123-x";
        x.saldo = 1000;
        System.out.println(x.titular + " " + x.numero + " " + x.saldo);
        x.depositar(500);
        System.out.println(x.titular + " " + x.numero + " " + x.saldo);
    }
}


