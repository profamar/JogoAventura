Contexto:
Este projeto consiste em desenvolver um jogo onde será criada uma classe genérica que represente um herói de uma aventura. Essa classe deve incluir os seguintes elementos de programação: variáveis, operadores, laços de repetição, estruturas de decisão, funções, classes e objetos. O principal objetivo é criar essa classe genérica, garantindo que ela represente adequadamente um herói, e implementar o método atacar, conforme as especificações descritas no formato abaixo:

Descrição da Classe do Heroi:
' ' '
class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        print(f"Heroi criado: {self.nome}, {self.idade} anos, tipo: {self.tipo}")

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
print("Criando heroi1")
heroi1 = Heroi("Arthur", 30, "guerreiro")
heroi1.atacar()  # Saída: o guerreiro usou espada

print("Criando heroi2")
heroi2 = Heroi("Merlin", 150, "mago")
heroi2.atacar()  # Saída: o mago usou magia

print("Script executado com sucesso")

' ' '
Requesitos:
Python 3.x

Como usar:
1- Clone o repositório. 
2-Navegue até o diretório do projeto.
3- Execute o script heroi.py para ver os exemplos de uso. git clone cd JogoAventura python heroi.py



