class Produto:
    produtos_cadastrados = [] 

    def __init__(self, descricao, codigo_barras, custo, preco_venda, fornecedor, categoria):
        self.descricao = descricao
        self.codigo_barras = codigo_barras
        self.custo = custo
        self.preco_venda = preco_venda
        self.fornecedor = fornecedor
        self.categoria = categoria
    
    def cadastrar_produto(self):
        produto_info = {
            "descricao": self.descricao,
            "codigo_barras": self.codigo_barras,
            "custo": self.custo,
            "preco_venda": self.preco_venda,
            "fornecedor": self.fornecedor,
            "categoria": self.categoria
        }

        self.produtos_cadastrados.append(produto_info)
        print("Produto cadastrado com sucesso!")



if __name__ == '__main__':
    pass
