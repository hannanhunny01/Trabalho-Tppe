# usuario.py
class Usuario:
    def __init__(self, nome, telefone, email, senha):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.senha = senha

    def exibir_informacoes(self):
        return f"Nome: {self.nome}\nTelefone: {self.telefone}\nEmail: {self.email}"
