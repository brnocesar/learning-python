import json, re


# valida url e extrai parâmetros
url = 'https://bytebank.com/cambio?moeda_origem=real&moeda_destino=dolar&quantidade=100'
# url = 'https://bytebank/cambio?moeda_origem=real&moeda_destino=dolar&quantidade=100'
# url = ' \t'

# sanitização da url
url = url.strip().replace(' ', '')

# verifica se foi passada uma string na url
if url == "":
    raise ValueError("A URL está vazia!")
else:
    print("=> A URL não está vazia!")

# fatiamento da url
url_fatiada    = url.split('?')
url_base       = url_fatiada[0]
url_parametros = url_fatiada[1]

# valida url
recursos   = ['cambio', 'cotacao', 'simulacao'] # recursos que podem ser acessados nessa url
padrao_url = f"^(http(s)?:\/\/)?(www.)?bytebank\.com(\.br)?\/({'|'.join(recursos)})$"
resultado  = re.match(padrao_url, url_base) # verifica se a string completa bate com o padrão, se são exatamente "iguais"
if not resultado:
    raise ValueError("A URL é inválida!")
else:
    print(f"=> {resultado}\n=> A URL é válida!")

# extrai parâmetros da url
parametros_url = {}
for i in url_parametros.split('&'):
    j = i.split('=')
    if len(j) == 2:
        parametros_url[j[0]] = j[1]

print(f"""=> url completa:\t{url}
=> url fatiada:\t\t{url_fatiada}
=> url base:\t\t{url_base}
=> parâmetros na url:\t{url_parametros}
=> parâmetros da url em um dicionário:\n{json.dumps(parametros_url, sort_keys=True, indent=4)}
"""
)



# procura CEP em endereço
endereco = "Rua dos Alfeneiros 4, Ipaneminha, Belo Horizonte, BA, 12345-678"

# abordagem 1
padrao   = re.compile("\d{5}[-]?\d{3}")
busca    = padrao.search(endereco) # procura pelo padrao dentro da string endereco

# abordagem 2
busca    = re.search("\d{5}[-]?\d{3}", endereco) # procura pelo padrao dentro da string endereco

cep = busca.group() if busca else 'CEP não encontrado' # metodo group() retorna primeira ocorrência do padrão
print(f"\n\n||> endereço:\t{endereco}\n||> cep encontrado: {cep}")