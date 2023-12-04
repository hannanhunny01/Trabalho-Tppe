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
