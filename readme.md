# learning-python

## 1. Introdução

- i/o na saída padrão
- tipos de dados
- estruturas de controle
- _built-in functions_
- funções
- módulos externos
- contentores
- compreensão de listas
- i/o de arquivos

## 2. Orientação a objetos

- Classes, objetos e `self`
- Propriedades e métodos
  - _Dunder methods_ (métodos especiais)
    - Função "construtora" (`__init__`)
    - Representação textual de um objeto (`__str__`)
    - Representação lógica de um objeto(`__repr__`)
  - métodos e atributos estáticos
- Encapsulamento e coesão do código
  - `__` vs `_`
- Polimorfismo
  - Herança (extensão)
    - Relacionamento "é um..."
    - método `super()`
    - Herança de tipos _built in_
    - Interface vs Reuso (vantagens e desvantagens) 
- Composição
  - Relacionamento "tem um..."/"se comporta como um..."
  - _Duck typing_ e _magic methods_
    - `__getitem__`, `__len__`
    - _Python data (object) model_: inicialização, representação, container, numéricos
- Classes abstratas
  - Interfaces: _Abstract Base Classes_ (ABC)
  - Métodos abstratos
- Herança múltipla
  - _Method Resolution Order_ (MRO)
  - Mixins

## 3. _Strings_

- O que são _strings_?
- Fatiando _strings_
- Expressões regulares
- Métodos especiais

## 4 Collections

- Listas
- Tuplas
- Lista de tuplas
- Tupla de objetos
- Heraça e polimorfismo
- _Array_ e Numpy
- Igualdade e o `__eq__`
- Outras _built in functions_
  - `enumerate`
  - `range`
  - desempacotamento de tuplas
- Ordenação
  - _in place_
  - _lazy loading_
  - ordem natural
    - `__lt__` (_less than_)
  - _functools_
    - `total_ordering`
- Conjuntos
- Dicionários

## 5 Validação de dados nacionais

- Validação de CPF e CNPJ com pacotes externos
- Expressões regulares
  - Telefone
  - E-mail
- Datas
  - biblioteca `datetime`
- CEP
  - usando um _web service_

## 6 Testes

- Teste de unidade
  - TDD e boas práticas
  - Biblioteca `unittest`
    - cenários isolados (`setUp()`)
  - Biblioteca `pytest`
    - cenários isolados (_fixtures_ e injeção de dependências)
  - Classes de equivalência
  - Gerenciador de contextos (`with`)
  - Exceções
