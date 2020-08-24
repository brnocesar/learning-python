class Conta:

    taxa = 13.9
    
    def __init__(self, numero, titular, saldo, limite=1000.0):
        print("=> contruindo objeto... {}".format(self))
        self.__numero       = numero 
        self.__titular      = titular
        self.__saldo        = saldo
        self.__limite       = limite

    @staticmethod
    def codigo_bancos():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    
    def extrato(self):
        print("=> Saldo do titular {}: {}".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor
        return self

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_para_saque = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_para_saque

    def saca(self, valor_a_sacar):
        if (self.__pode_sacar(valor_a_sacar)):
            self.__saldo -= valor_a_sacar
        else:
            print("=> O valor de {} ultrapassa o limite.".format(valor_a_sacar))
        return self

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    