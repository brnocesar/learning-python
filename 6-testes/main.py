from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

bruno = Usuario('bruno')
bruna = Usuario('bruna')

lance_do_bruno = Lance(bruno, 100.0)
lance_da_bruna = Lance(bruna, 150.0)

leilao = Leilao('Video Game')
leilao.lances.append(lance_do_bruno)
leilao.lances.append(lance_da_bruna)

for lance in leilao.lances:
    print(f"O usuário {lance.usuario.nome} deu um lance de {lance.valor}")

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f"O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}")
