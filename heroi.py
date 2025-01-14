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
