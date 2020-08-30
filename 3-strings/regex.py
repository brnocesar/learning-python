import re

print("Telefone celular")
contato_um = "Meu número é 91234-1234, tem também o 998764321 e não se esqueça do 94567-8912"
contato_dois = "Fale comigo através de 94567-8912 esse é o meu telefone"
contato_tres = "99876-4321 é o meu telefone"

padrao = "9[0-9]{4}[-]*[0-9]{4}"

retorno = re.search(padrao, contato_um) # pega apenas a primeira ocorrencia
print(f"=> objeto: {retorno}")
print("=> search()  - retorno:", retorno.group()) # e se não encontrar o padrao?

retorno = re.findall(padrao, contato_um)
print("=> findall() - retorno: {}".format(retorno))
