class Loja:

    lojas_cadastradas = []
    
    def __init__(self, nome, cnpj, endereco, representante, estoques):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.representante = representante
        self.estoques = estoques

    def cadastrar_loja(self):
        pass

    def editar_loja(self, cnpj, dados):
        pass

    def remover_loja(self, cnpj):
        pass

    def listar_lojas(self):
        pass

    def buscar_loja_nome(self, nome):
        pass
