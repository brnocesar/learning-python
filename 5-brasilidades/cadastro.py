from datetime import datetime, timedelta

class Cadastro:
    
    def __init__(self):
        tempo_cadastrado = 30 # random
        self.momento_cadastro = datetime.today() - timedelta(days=tempo_cadastrado)
    
    def __str__(self):
        return self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
    
    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março", "abril",
            "maio", "junho", "julho", "agosto",
            "setembro", "outubro", "novembro", "dezembro"
        ]
        return meses_do_ano[self.momento_cadastro.month - 1]
    
    def dia_semana_cadastro(self):
        dias_da_semana = [
            "segunda-feira", "terça-feira", "quarta-feira",
            "quinta-feira", "sexta-feira", "sábado", "domingo"
        ]
        return dias_da_semana[self.momento_cadastro.weekday()]
    
    def tempo_cadastro(self):
        # simula cadastro realizado a trinta dias
        return datetime.today() - self.momento_cadastro
