from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://meusitebonito.com.br/recurso?param1=valor1&param2=valor2&param3=valor3"

argumentos_um = ExtratorArgumentosUrl(url)
argumentos_dois = ExtratorArgumentosUrl(url)

print(argumentos_um == argumentos_dois)
print("ID de cada instância:", id(argumentos_um), id(argumentos_dois))
print("Representação de uma instância:", argumentos_um)
