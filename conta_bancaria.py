class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def extrato(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo atual: R${self.saldo:.2f}")


# Exemplo de uso do sistema bancário
if __name__ == "__main__":
    conta1 = ContaBancaria("João", 1000)

    conta1.depositar(500)
    conta1.sacar(200)
    conta1.extrato()
