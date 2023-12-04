class Fornecedor:
    
    fornecedores_cadastrados = []

    def __init__(self, nome):
        self.nome = nome

    def cadastrar_fornecedor(self):
        
        for fornecedor in Fornecedor.fornecedores_cadastrados:
            if fornecedor.nome == self.nome:
                print(f"O fornecedor '{self.nome}' já existe!")
                return False

        if self.nome.strip() == "":
            print("Nome do fornecedor não pode ser vazio!")
            return False

        novo_fornecedor = Fornecedor(self.nome)
        Fornecedor.fornecedores_cadastrados.append(novo_fornecedor)
        print(f"Fornecedor '{self.nome}' cadastrado com sucesso!")

    def remover_fornecedor(self, codigo_fornecedor):
        for fornecedor in self.fornecedores_cadastrados:
            if fornecedor["codigo_fornecedor"] == codigo_fornecedor:
                Fornecedor.fornecedores_cadastrados.remove(fornecedor)
                print(f"Fornecedor com código {codigo_fornecedor} removido com sucesso.")
                return True
        
        print(f"Fornecedor com código {fornecedor} não encontrado.")
        return False

    def editar_fornecedor(self, novo_nome):
        for fornecedor in Fornecedor.fornecedores_cadastrados:
            if fornecedor.nome == self.nome:
                fornecedor.nome = novo_nome
                print(f"Fornecedor '{self.nome}' editado com sucesso!")
                return True

        print(f"O fornecedor '{self.nome}' não existe!")
        return False