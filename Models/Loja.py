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
        loja = {
            "nome": self.nome,
            "cnpj": self.cnpj,
            "endereco": self.endereco,
            "representante": self.representante,
            "estoques": self.estoques,
            "funcionarios": self.funcionarios
        }
        self.lojas_cadastradas.append(loja)

    def editar_loja(self, cnpj, dados):
        for loja in self.lojas_cadastradas:
            if loja["cnpj"] == cnpj:
                for key, value in dados.items():
                    loja[key] = value
                return loja

    def remover_loja(self, cnpj):
        for loja in self.lojas_cadastradas:
            if loja["cnpj"] == cnpj:
                self.lojas_cadastradas.remove(loja)

    def listar_lojas(self):
        return self.lojas_cadastradas

    def buscar_loja_nome(self, nome):
        for loja in self.lojas_cadastradas:
            if loja["nome"] == nome:
                return loja

    def associar_funcionario(self, cpf):
        for loja in self.lojas_cadastradas:
            if loja["cnpj"] == self.cnpj:
                loja["funcionarios"].append(cpf)
    
    def desassociar_funcionario(self, cpf):
        for loja in self.lojas_cadastradas:
            if loja["cnpj"] == self.cnpj:
                loja["funcionarios"].remove(cpf)
    
    def associar_representante(self, cpf):
        for loja in self.lojas_cadastradas:
            if loja["cnpj"] == self.cnpj:
                loja["representante"] = cpf