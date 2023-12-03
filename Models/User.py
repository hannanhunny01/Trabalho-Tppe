# usuario.py
class Usuario:
    def __init__(self, nome, telefone, email, senha):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.senha = senha

    def exibir_informacoes(self):
        return f"Nome: {self.nome}\nTelefone: {self.telefone}\nEmail: {self.email}"



class Gerente(Usuario):
    def __init__(self, nome, telefone, email, senha, cpf, lojas):
        super().__init__(nome, telefone, email, senha)
        self.cpf = cpf
        self.lojas = lojas

    def exibir_informacoes_gerente(self):
        return f"{super().exibir_informacoes()}\nCPF: {self.cpf}\nLojas: {', '.join(self.lojas)}"


class Funcionario(Usuario):
    def __init__(self, nome, telefone, email, senha, cpf, loja):
        super().__init__(nome, telefone, email, senha)
        self.cpf = cpf
        self.loja = loja

    def exibir_informacoes_funcionario(self):
        return f"{super().exibir_informacoes()}\nCPF: {self.cpf}\nLoja: {self.loja}"
