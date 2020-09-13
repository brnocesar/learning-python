from cadastro_de_pessoa import CadastroDePessoa
from factory_documento import Documento, Cpf, Cnpj
from contato import Telefone, Email
from endereco import Endereco
from cadastro import Cadastro
import datetime

documento = input("=> Digite o CPF/CNPJ: ")
ddi       = input("=> Código de área internacional: ")
ddd       = input("=> Código de área estadual: ")
telefone  = input("=> Digite o telefone: ")
email     = input("=> Digite o endereço de email: ")
cep       = input("=> Digite o CEP do seu endereço: ")

print("\nValidando dados...\n")
# print("CPF/CNPJ: {} \t (válido)", Documento.cria_documento(documento)) # factory
print(f"válido...\tCPF/CNPJ:\t{CadastroDePessoa(documento)}")
print("válido...\tTelefone:\t{}".format(Telefone(ddi, ddd, telefone)))
print(f"válido...\tEmail:\t\t{Email('bruno@mail.com')}")
print("válido...\tEndereço:\t{}".format(Endereco('81050-675')))
print(f"ok...\t\tCliente desde:\t{Cadastro().tempo_cadastro()}")
