import json, re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url_passada()
        self.separa_url()
        self.valida_padrao_url()
        
    def sanitiza_url(self, url):
        return url.strip() if isinstance(url, str) else ""
    
    def valida_url_passada(self):
        if not self.url:
            raise ValueError("A URL está vazia!")
    
    def valida_padrao_url(self):
        recursos   = ['cambio', 'cotacao', 'simulacao']
        padrao_url = f"^(http(s)?:\/\/)?(www.)?bytebank\.com(\.br)?\/({'|'.join(recursos)})$"
        resultado  = re.match(padrao_url, self.url_base)
        if not resultado:
            raise ValueError("A URL é inválida!")
    
    def separa_url(self):
        url_fatiada    = self.url.split('?')
        self.url_base  = url_fatiada[0]
        url_parametros = url_fatiada[1]
        self.parametros_url = {}
        for i in url_parametros.split('&'):
            j = i.split('=')
            if len(j) == 2:
                self.parametros_url[j[0]] = j[1]
    
    def get_valor_parametro(self, parametro):
        return self.parametros_url.get(parametro, 'Parâmetro não encontrado!')
    
    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return f"=> URL base:\n{self.url_base}\n=>Parâmetros:\n{json.dumps(parametros_url, sort_keys=True, indent=4)}"
    
    def __eq__(self, other):
        return self.url == other.url
    

url_teste = 'https://bytebank.com/cambio?moeda_origem=real&moeda_destino=dolar&quantidade=100'
# instancia objeto
extrator_url = ExtratorURL(url_teste)
print(extrator_url.get_valor_parametro('moeda_origem'))
print(extrator_url.get_valor_parametro('batatinha'))

print(len(extrator_url))
print(extrator_url) # imprime tipo e endereço de memória como comportamento padrão

# instancia outro objeto com a mesma url
extrator_url_2 = ExtratorURL(url_teste)
# compara endereço de memória como comportamento padrão, recebe o que vai comparar: extrator_url.__eq__(extrator_url_2)
print(extrator_url == extrator_url_2)
print(id(extrator_url), id(extrator_url_2))