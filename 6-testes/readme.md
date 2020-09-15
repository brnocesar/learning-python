# testes

- Teste de unidade
  - TDD e boas práticas
  - Biblioteca `unittest`
    - cenários isolados (`setUp()`)
  - Biblioteca `pytest`
    - cenários isolados (_fixtures_ e injeção de dependências)
  - Classes de equivalência
  - Gerenciador de contextos (`with`)
  - Exceções

## Rodando testes de unidade com `unittest`

Se você não está usando o PyCharm ou alguma extensão para o VSCode, provavelmente apenas apertar o botãozinho **"Run"** não vai ser a melhor forma de rodar os testes. Abaixo são apresentados alguns comandos úteis para isso.

### Rodando testes específicos

#### Usando o executável do Python

Você pode rodar o teste a partir do próprio executável do Python. Basta que você avalie o valor de `__name__` ao final do arquivo e se for `'__main__'` chamar a função `main()`:

```terminal
python3 <path>/test_<classe testada>.py
```

Alguns detalhes devem ser observados nessa abordagem:

- o caminho utilizado para importar as classes testadas deve ser relativo ao local das classes testadas.
- é necessário importar o método `main` da biblioteca `unittest`. Se optar por "apenas" importar a biblioteca toda, não se esqueça de acessar a classe `TestCase` e o método `main()` a partir da biblioteca importada (`unittest.TestCase` e `unittest.main()`, respectivamente).  
Considerando que as classes testadas então no arquivo `dominio.py`, o arquivo do teste está no mesmo diretório e o comando será rodado, abaixo são apresentados os _layouts_ de como o arquivo deve se parecer:

```python
import unittest
from dominio import Usuario, Lance, Leilao, Avaliador

class TestAvaliador(unittest.TestCase):
    def test_avalia(self):
        # implementação testada

if __name__ == '__main__':
    unittest.main()
```

```python
from unittest import TestCase, main
from dominio import Usuario, Lance, Leilao, Avaliador

class TestAvaliador(TestCase):
    def test_avalia(self):
        # implementação testada

if __name__ == '__main__':
    main()
```

#### Usando o módulo de testes

O módulo de testes (`unittest`) fornece uma interface por linha de comando (CLI, sigla em inglês) que permite executar diversas tarefas, entre elas rodar o teste para uma classe específica:

```terminal
python3 -m unittest <path>/test_<classe testada>.py
```

Nessa abordagem não é necessário executar o método `main()`, o módulo de testes se encarrega disso. Agora é preciso se atentar para o caminho de importação das classes testadas, que vai depender do local em que o comando está sendo executado:

- se comando for executado na raiz do projeto, a inclusão deve ser feita em relação a raiz:

```python
from unittest import TestCase, main
from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

class TestAvaliador(TestCase):
    def test_avalia(self):
        # implementação testada
```

```terminal
$ python3 -m unittest src/leilao/test_avaliador.py
```

- agora, se o comando é executado no local em que os arquivos estão, a inclusão deve ser feita em relação a este local:

```python
from unittest import TestCase, main
from dominio import Usuario, Lance, Leilao, Avaliador

class TestAvaliador(TestCase):
    def test_avalia(self):
        # implementação testada
```

```terminal
src/leilao$ python3 -m unittest test_avaliador.py
```

##### Rodando métodos específicos de um teste

### Rodando vários testes

Quando executamos o módulo de testes pela CLI podemos utilizar a _flag_ `discover` passando um diretório, assim todos os testes nesse diretório serão executados:

```terminal
python3 -m unittest discover <path>
```

## Rodando testes de unidade com `pytest`

O `pytest` tem o objetivo ajudar a escrever testes de forma mais simples, ele pretende ser mais simples e isso já pode ser visto quando começamos a escrever os testes.

Ao contrário do `unittest` que precisamos criar uma classe extendendo a `TestCase`, para dai sim começar a escrever os métodos de cada teste, com o `pytest` podemos escrever apenas o método do teste e já sair testando.

Como não estamos herdando funcionalidades de uma classe de testes precisamos fazer algumas adaptações. No caso do teste de asserção agora precisamos usar a palavra reservada do Python, `assert`.

O comando para executar os testes pode diferir de acordo com seu sistema operacional e/ou a forma como foi feita a instalação da biblioteca. Inicialmente você pode tentar:

```terminal
pytest
```

Se esse não funcionar, deve ser porque a biblioteca está instalada apenas para o python (?), então você deve executar através do executável do python:

```terminal
python3 -m pytest
```
