from validate_docbr import CPF, CNPJ

class CadastroDePessoa:
    
    def __init__(self, documento):
        documento = str(documento).replace('.', '').replace('-', '').replace('/', '')
        
        if self.documento_valido(documento):
            self.numero = documento
            return
        raise ValueError("Documento inválido!")
    
    
    def __str__(self):
        return CPF().mask(self.numero) if len(self.numero) == 11 else CNPJ().mask(self.numero)


    def documento_valido(self, documento):
        if len(documento) == 11:
            return CPF().validate(documento)
        if len(documento) == 14:
            return CNPJ().validate(documento)
        raise ValueError("Documento com quantidade de dígitos inválida!")
