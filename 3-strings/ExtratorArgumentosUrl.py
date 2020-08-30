class ExtratorArgumentosUrl:
    def __init__(self, url):
        url_eh_valida = self.valida_url_estatico(url)
        # url_eh_valida = self.valida_url_nao_estatico(url)
        
        if url_eh_valida:
            self.url = url
        else:
            raise ValueError("url inválida!!!") # trocar o tipo de erro


    def __str__(self):
        representacao_param_val = "alguma coisa"
        return str(self.extrai_argumentos())


    def __len__(self):
        return len(self.url)


    def __eq__(self, outra_instancia):
        return self.url == outra_instancia.url


    def valida_url_nao_estatico(self, url):
        if url and url.startswith("https://meusitebonito.com.br"):
            return True
        else:
            return False


    @staticmethod
    def valida_url_estatico(url):
        if url and url.startswith("https://meusitebonito.com.br"):
            return True
        else:
            return False


    def extrai_argumentos(self):
        partes_da_url = self.url.split('?')
        if len(partes_da_url) <= 1:
            return "Não há argumentos."
        
        lista_argumentos      = partes_da_url[1].split('&')
        dicionario_argumentos = {}
        for argumento in lista_argumentos:
            parzinho = argumento.split('=')
            if len(parzinho) != 2:
                continue
            dicionario_argumentos[parzinho[0]] = parzinho[1]
        
        if not dicionario_argumentos:
            return "Não há argumentos."
        
        return dicionario_argumentos
