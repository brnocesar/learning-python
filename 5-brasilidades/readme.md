# brasilidades

- Validação de CPF e CNPJ com pacotes externos
- Expressões regulares
  - Telefone
  - E-mail
- Datas
- CEP

## Validação de CPF e CNPJ com pacotes externos

Existem vários pacotes destinados a validar números de CPF e CNPJ, neste caso foi usado o pacote [`validate_docbr`](https://pypi.org/project/validate-docbr/).

[Aqui](https://github.com/brnocesar/learning-PHP/blob/main/16-brasilidades/models/Cpf.php) e [aqui](https://github.com/brnocesar/learning-PHP/blob/main/16-brasilidades/models/Cnpj.php) tem implementações completas da validação desses documentos, CPF e CNPJ, feitas em PHP.

## Expressões regulares

### Telefone

O padrão completo para validar um número de telefone com códigos internacional e estadual é:

```regex
^(\+\d{2,3}\s?)?((\(\d{2}\))|(\d{2}))\s?9?\d{4}\-?\d{4}$
```

regex|descrição|significado
:-:|-|-
`^(\+\d{1,3}\s?)?` | deve começar com um a três inteiros precedendo um sinal `+` com um espaçamento opcinal | código de área internacional
`((\(\d{2}\))|(\d{2}))` | dois inteiros, envolvidos ou não por parênteses | código de área estadual
\s? | espaçamento | -
9? | número 9 | para celulares
\d{4} | quatro inteiros | -
\-? | caracter especial traço | -
\d{4} | deve terminar com quatro inteiros | -

### Datas

- Paramêtros para o método `srtftime()`

  - `%A` retorna os dias da semana por extenso em inglês;
  - `%d` exibe os dias do mês com números de 01 a 31;
  - `%m` retorna meses em números de 01 a 12;
  - `%y` mostra o ano com apenas dois dígitos;
  - `%Y` apresenta o ano em formato de quatro números;
  - `%H` retorna o horário no formato decimal, de 00 a 23;
  - `%M` exibe os minutos de forma decimal, de 00 a 59;
  - `%S` apresenta os segundos em decimal, de 00 a 59.
