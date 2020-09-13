from validate_docbr import CPF, CNPJ

class Documento:
    @staticmethod
    def cria_documento(documento):
        documento = str(documento).replace('.', '').replace('-', '').replace('/', '')
        
        if len(documento) == 11:
            return Cpf(documento)
        if len(documento) == 14:
            return Cnpj(documento)
        raise ValueError("Documento inválido!")


class Cpf:
    def __init__(self, documento):
        if self.cpf_valido(documento):
            self.numero = documento
            return
        raise ValueError("CPF inválido!")
    
    def __str__(self):
        return self.formata_numero()

    def cpf_valido(self, documento):
        return CPF().validate(documento)
    
    def formata_numero(self):
        return CPF().mask(self.numero)


class Cnpj:
    def __init__(self, documento):
        if self.cnpj_valido(documento):
            self.numero = documento
            return
        raise ValueError("CNPJ inválido!")
    
    def __str__(self):
        return self.formata_numero()

    def cnpj_valido(self, documento):
        return CNPJ().validate(documento)
    
    def formata_numero(self):
        return CNPJ().mask(self.numero)
