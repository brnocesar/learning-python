import re
import requests

class Endereco:
    
    def __init__(self, cep):
        self.cep      = self.valida_cep(str(cep))
        self.endereco = self.recupera_endereco()
        return
    
    def __str__(self):
        resposta = re.search("(\d{5})(\d{3})", self.cep)
        return "{}, {}, {}/{} - {}-{}".format(
            self.endereco['logradouro'], self.endereco['bairro'], self.endereco['localidade'], 
            self.endereco['uf'], resposta.group(1), resposta.group(2)
        )
    
    def valida_cep(self, cep):
        resposta = re.search("^\d{5}\-?\d{3}$", cep)
        if resposta == None:
            raise ValueError("CEP em formato inválido!")
        return resposta.group().replace("-", "")
    
    def recupera_endereco(self):
        r = requests.get(f"https://viacep.com.br/ws/{self.cep}/json/")
        resposta = r.json()
        if "erro" in resposta:
            raise ValueError("CEP não corresponde a endereço!")
        
        return {chave: valor for chave, valor in resposta.items() if chave in ['logradouro', 'bairro', 'localidade', 'uf']}
