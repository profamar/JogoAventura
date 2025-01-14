# Jogo de Aventura em Python

# Desafio de Projeto do Bootcamp GFT Start #6 - Lógica de Programação

## Introdução
Bem-vindo ao projeto Jogo de Aventura em Python! Este projeto foi criado para praticar conceitos de programação, incluindo variáveis, operadores, laços de repetição, estruturas de decisão, funções, classes e objetos.
Este projeto é um ótimo ponto de partida para explorar a criação de jogos em Python. Sinta-se à vontade para expandir e melhorar este projeto.

## Objetivo
Criar uma classe genérica que represente um herói em uma aventura e implementar o método `atacar` conforme descrito abaixo.

## Estrutura do Projeto
JogoAventura/
│
├── README.md          # Documentação do projeto
├── heroi.py           # Código fonte da classe Heroi
├── config/            # Arquivos de configuração (se necessário)
├── scripts/           # Scripts individuais de automação (se necessário)
├── logs/              # Arquivos de log (se necessário)
└── data/              # Arquivos de dados (ex: arquivos CSV, se necessário)


## Requisitos
- Python 3.x
## Como Usar
1- Clone o repositório.
2-Navegue até o diretório do projeto.
3- Execute o script heroi.py para ver os exemplos de uso.
git clone <URL-do-repositorio>
cd JogoAventura
python heroi.py

## Descrição da Classe `Heroi`

```python
class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        ataques = {
            "mago": "usou magia",
            "guerreiro": "usou espada",
            "monge": "usou artes marciais",
            "ninja": "usou shuriken"
        }
        ataque = ataques.get(self.tipo, "usou um ataque desconhecido")
        print(f"o {self.tipo} {ataque}")

# Exemplo de uso
heroi1 = Heroi("Arthur", 30, "guerreiro")
heroi1.atacar()  # Saída: o guerreiro usou espada

heroi2 = Heroi("Merlin", 150, "mago")
heroi2.atacar()  # Saída: o mago usou magia
