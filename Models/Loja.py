class Loja:

    lojas_cadastradas = []

    def __init__(self, nome, cnpj, endereco, representante, estoques, funcionarios):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.representante = representante
        self.estoques = estoques
        self.funcionarios = funcionarios

    def cadastrar_loja(self):

        for loja in self.lojas_cadastradas:
            if loja['nome'] == self.nome:
                print(f"A loja '{self.nome}' já existe!")
                return False

        if self.nome.strip() == "":
            print("Nome da loja não pode ser vazio!")
            return False

        loja = {
            "nome": self.nome,
            "cnpj": self.cnpj,
            "endereco": self.endereco,
            "representante": self.representante,
            "estoques": self.estoques,
            "funcionarios": self.funcionarios
        }
        self.lojas_cadastradas.append(loja)
        print(f"Loja '{self.nome}' cadastrada com sucesso!")
        return True

    def remover_loja(self):
        for loja in self.lojas_cadastradas:
            if loja['nome'] == self.nome:
                self.lojas_cadastradas.remove(loja)
                print(f"Loja '{self.nome}' removida com sucesso!")
                return True

        print(f"A Loja '{self.nome}' não existe!")
        return False

    def editar_loja(self, cnpj, dados):
        for loja in self.lojas_cadastradas:
            if loja["cnpj"] == cnpj:
                for key, value in dados.items():
                    loja[key] = value
                print(f"Loja '{self.nome}' editada com sucesso!")
                return True

        print(f"A loja '{self.nome}' não existe!")
        return False
    
    def obter_loja_por_nome(self, nome):
        for loja in self.lojas_cadastradas:
            if loja['nome'] == nome:
                print(f"Loja '{self.nome}' encontrada!")
                return loja
        return False

    def listar_lojas(self):
        return self.lojas_cadastradas