# fatiando meu nome
meu_nome = "Bruno Cesar"
primeiro = meu_nome[:5] # meu_nome[0:5]
segundo = meu_nome[6:]
print(f"Meu primeiro nome: '{primeiro}'\nMeu segundo nome: '{segundo}'")


# fatiando uma url
url = "https://meusitebonito.com.br/recurso?PARAM1=valor1&param2=valor2&paRam3=valor3"
separador = url.find('?')
argumentos = url[separador + 1:]
print("Os parâmetros passados na URL são: {}".format(argumentos))

lista_argumentos = argumentos.split('&')
print("Lista de argumentos da URL: ", lista_argumentos)

dicionario_argumentos = {}
for argumento in lista_argumentos:
    duplinha = argumento.split('=')
    print(duplinha)
    dicionario_argumentos[duplinha[0]] = duplinha[1]

print(dicionario_argumentos)
for elemento in dicionario_argumentos:
    print(elemento, dicionario_argumentos[elemento])

parametros = list(map(lambda item_da_lista: item_da_lista.lower(), dicionario_argumentos.keys()))
valores    = list(dicionario_argumentos.values())
print("Os parâmetros são: {1} e seus valores: {0}".format(valores, parametros))

tupla_valores = tuple(valores)
tupla_parametros = tuple(parametros)
print(tuple(valores))
print(tuple(parametros))
valor_um, valor_dois, valor_tres = tupla_valores
print("param 1 = {primeiro}\tparam 2 = {segundo}\tparam 3 = {terceiro}\t".format(primeiro=valor_um, segundo=valor_dois, terceiro=valor_tres))