
# 🛡️ Jogo de Aventura: Classe Genérica de Herói

Este projeto consiste em criar uma classe genérica que representa um herói de uma aventura. A classe inclui elementos essenciais de programação como variáveis, operadores, laços de repetição, estruturas de decisão, funções, classes e objetos. 

## 🧾 Descrição do Projeto

A classe `Heroi` é projetada para modelar personagens heróicos com atributos básicos e funcionalidades específicas. Um destaque é o método `atacar`, que simula diferentes estilos de ataque baseados no tipo do herói.

### Estrutura da Classe
```python
class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        print(f"Herói criado: {self.nome}, {self.idade} anos, tipo: {self.tipo}")

    def atacar(self):
        ataques = {
            "mago": "usou magia",
            "guerreiro": "usou espada",
            "monge": "usou artes marciais",
            "ninja": "usou shuriken"
        }
        ataque = ataques.get(self.tipo, "usou um ataque desconhecido")
        print(f"O {self.tipo} {ataque}")


### Exemplos de Uso
```python
# Criando um herói do tipo guerreiro
heroi1 = Heroi("Arthur", 30, "guerreiro")
heroi1.atacar()  # Saída: O guerreiro usou espada

# Criando um herói do tipo mago
heroi2 = Heroi("Merlin", 150, "mago")
heroi2.atacar()  # Saída: O mago usou magia
```

## 🛠️ Requisitos

- Python 3.x instalado no sistema.

## 📋 Como Usar

Siga as etapas abaixo para rodar o projeto localmente:

1. **Clone o Repositório**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```
2. **Navegue até o Diretório do Projeto**
   ```bash
   cd JogoAventura
   ```
3. **Execute o Script**
   ```bash
   python heroi.py
   ```

## 🚀 Funcionalidades

- **Criação de Heróis**: Adicione heróis personalizados com nome, idade e tipo.
- **Ações**: Cada herói pode realizar ataques diferentes, dependendo do tipo atribuído.
- **Mensagens Informativas**: O script exibe mensagens claras sobre a criação do herói e os ataques realizados.

## 📂 Estrutura do Repositório

```
JogoAventura/
├── heroi.py         # Código principal do projeto
├── README.md        # Documentação do projeto
```

## 🌟 Contribuições

Sinta-se à vontade para contribuir com melhorias ou novas funcionalidades! 

1. Faça um fork do repositório.

2. Crie um branch para suas alterações:
   ```bash
   git checkout -b minha-feature
   ```
3. Commit suas alterações:
   ```bash
   git commit -m 'Adiciona nova funcionalidade'
   ```
4. Envie para o repositório principal:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

## 📝 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

## 📧 Contato

Para dúvidas ou sugestões, entre em contato pelo Linkedin: [linkedin.com/in/márcia-soares-236974256)

