from unittest import TestCase, main
from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.excecoes import LanceInvalido

class TestLeilao(TestCase):
    
    def setUp(self):
        self.valor_carteira       = 1000.0
        self.menor_valor_esperado = 100.0
        self.maior_valor_esperado = 150.0
        self.usuario_bruno        = Usuario('bruno', self.valor_carteira)
        self.lance_do_bruno       = Lance(self.usuario_bruno, self.menor_valor_esperado)
        self.lance_da_bruna       = Lance(Usuario('bruna', self.valor_carteira), self.maior_valor_esperado)
        self.leilao               = Leilao('Video Game')


    def test_quando_adiciona_dois_lances_em_ordem_crescente_deve_retornar_os_de_maior_e_menor_valor(self):
        
        self.leilao.propoe(self.lance_do_bruno)
        self.leilao.propoe(self.lance_da_bruna)
        
        self.assertEqual(self.menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(self.maior_valor_esperado, self.leilao.maior_lance)
    
    
    # alguns testes deixam de ser necessários conforme o sistema evolui e implementa novas regras de negócio
    # def test_quando_adiciona_dois_lances_em_ordem_decrescente_deve_retornar_os_de_maior_e_menor_valor(self):
    #     self.leilao.propoe(self.lance_da_bruna)
    #     self.leilao.propoe(self.lance_do_bruno)
    #     self.assertEqual(self.menor_valor_esperado, self.leilao.menor_lance)
    #     self.assertEqual(self.maior_valor_esperado, self.leilao.maior_lance)
    #
    # eles devem ser modificados e aproveitados para validar as novas regras
    def test_quando_propor_lances_em_ordem_decrescente_nao_deve_permitir(self):
        
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_da_bruna)
            self.leilao.propoe(self.lance_do_bruno)


    def test_quando_adiciona_apenas_um_lance_deve_retornar_o_mesmo_valor_para_o_lance_de_maior_e_menor_valor(self):
        
        self.leilao.propoe(self.lance_da_bruna)
        
        self.assertEqual(self.maior_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(self.maior_valor_esperado, self.leilao.maior_lance)


    def test_quando_adiciona_tres_lances_deve_retornar_os_de_maior_e_menor_valor(self):

        valor_maior_ainda = 200.0
        self.leilao.propoe(self.lance_do_bruno)
        self.leilao.propoe(self.lance_da_bruna)
        self.leilao.propoe(Lance(Usuario('breno', self.valor_carteira), valor_maior_ainda))
        
        self.assertEqual(self.menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(valor_maior_ainda, self.leilao.maior_lance)

    
    def test_quando_nao_ha_lances_deve_permitir_propor_um_lance(self):
        
        self.leilao.propoe(self.lance_do_bruno)
        
        self.assertEqual(1, self.leilao.quantidade_lances)
    
    
    def test_quando_ultimo_usuario_for_diferente_deve_permitir_propor_lance(self):
        
        self.leilao.propoe(self.lance_do_bruno)
        self.leilao.propoe(self.lance_da_bruna)
        
        self.assertEqual(2, self.leilao.quantidade_lances)
    
    
    def test_quando_ultimo_usuario_for_o_mesmo_nao_deve_permitir_propor_lance(self):
        
        # try:
        #     self.leilao.propoe(self.lance_do_bruno)
        #     self.leilao.propoe(self.lance_do_bruno)
        #     self.fail(msg='Não lançou exceção.')
        # except LanceInvalido:
        #     self.assertEqual(1, self.leilao.quantidade_lances)
        
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_bruno)
            self.leilao.propoe(Lance(self.usuario_bruno, 500.0))
