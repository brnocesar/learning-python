import re

class Telefone:
    
    def __init__(self, ddi, ddd, telefone):
        self.ddi      = self.valida_ddi(ddi)
        self.ddd      = self.valida_ddd(ddd)
        self.telefone = self.valida_telefone(telefone)
        return
    
    def __str__(self):
        padrao = "(\+\d{1,3})(\d{2})(\d{5})(\d{4})" if len(self.telefone) == 9 else "(\+\d{1,3})(\d{2})(\d{4})(\d{4})"
        
        resposta = re.search(padrao, self.ddi + self.ddd + self.telefone)
        return "{} ({}) {}-{}".format(resposta.group(1), resposta.group(2), resposta.group(3), resposta.group(4))
    
    def valida_ddi(self, ddi):
        if ddi == "":
            return '+55'
        resposta = re.search("^\+\d{1,3}$", ddi)
        if resposta == None:
            raise ValueError("Código internaciona é inválido!")
        return resposta.group()
    
    def valida_ddd(self, ddd):
        resposta = re.search("^\d{2}$", ddd)
        if resposta == None:
            raise ValueError("Código estadual é inválido!")
        return resposta.group()
    
    def valida_telefone(self, telefone):
        resposta = re.search("^[9]?\d{4}(\s|\-)?\d{4}$", telefone)
        if resposta == None:
            raise ValueError("Número de telefone é inválido!")
        return resposta.group().replace("-", "").replace(" ", "")


class Email:
    
    def __init__(self, email):
        self.email = self.valida_email(email)
    
    def __str__(self):
        return self.email
    
    def valida_email(self, email):
        resposta = re.search("\w+@[a-z]+((\.[a-z]{2,3}$)|(\.[a-z]{3}\.[a-z]{2}$))", email)
        if resposta == None:
            raise ValueError("Endereço de Email é inválido!")
        return resposta.group()
