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
    
    def listar_gerentes(gerentes):
        return gerentes

    def salvar_gerente(self, gerentes):
        gerentes.append(self)
        return gerentes

    def atualizar_gerente(self, gerentes):
        for i, gerente in enumerate(gerentes):
            if gerente.email == self.email:
                gerentes[i] = self
                break
        return gerentes

    @staticmethod
    def excluir_gerente(email, gerentes):
        gerentes = [gerente for gerente in gerentes if gerente.email != email]
        return gerentes


class Funcionario(Usuario):
    def __init__(self, nome, telefone, email, senha, cpf, loja):
        super().__init__(nome, telefone, email, senha)
        self.cpf = cpf
        self.loja = loja

    def exibir_informacoes_funcionario(self):
        return f"{super().exibir_informacoes()}\nCPF: {self.cpf}\nLoja: {self.loja}"
    
    def listar_funcionarios(funcionarios):
        return funcionarios

    def salvar_funcionario(self, funcionarios):
        funcionarios.append(self)
        return funcionarios

    def atualizar_funcionario(self, funcionarios):
        for i, funcionario in enumerate(funcionarios):
            if funcionario.email == self.email:
                funcionarios[i] = self
                break
        return funcionarios

    @staticmethod
    def excluir_funcionario(email, funcionarios):
        funcionarios = [funcionario for funcionario in funcionarios if funcionario.email != email]
        return funcionarios
