from Categoria import Categoria
from Exceptions import DescricaoEmBrancoException, ValorInvalidoException

class Produto:
    produtos_cadastrados = [] 

    def __init__(self, descricao, codigo_barras, custo, preco_venda, fornecedor, categoria):
        self.descricao = descricao
        self.codigo_barras = codigo_barras
        self.custo = custo
        self.preco_venda = preco_venda
        self.fornecedor = fornecedor
        # self.categoria = categoria
        self.categoria = Categoria.obter_categoria_por_nome(categoria)
    
    def cadastrar_produto(self):
        if self.custo < 0 or self.preco_venda < 0:
            print("O custo e o preço de venda não podem ser negativos!")
            raise ValorInvalidoException("O custo e o preço de venda não podem ser negativos!")

        if self.categoria == False:
            print("A categoria informada não existe ou não foi cadastrada!")
            return False

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

    def remover_produto(self, codigo_barras):
        for produto in self.produtos_cadastrados:
            if produto["codigo_barras"] == codigo_barras:
                self.produtos_cadastrados.remove(produto)
                print(f"Produto com código de barras {codigo_barras} removido com sucesso.")
                return
        print(f"Produto com código de barras {codigo_barras} não encontrado.")

    def editar_produto(self, codigo_barras, novos_dados):
        for produto in self.produtos_cadastrados:
            if produto["codigo_barras"] == codigo_barras:
                produto.update(novos_dados)
                print(f"Produto com código de barras {codigo_barras} editado com sucesso.")
                return
        print(f"Produto com código de barras {codigo_barras} não encontrado.")






if __name__ == '__main__':
    pass

