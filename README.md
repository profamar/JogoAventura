# Jogo de Aventura em Python

## Introdução
Bem-vindo ao projeto Jogo de Aventura em Python! Este projeto foi criado para praticar conceitos de programação, incluindo variáveis, operadores, laços de repetição, estruturas de decisão, funções, classes e objetos.

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
