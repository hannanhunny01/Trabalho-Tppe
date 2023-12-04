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
        self.categoria = Categoria.obter_categoria_por_nome(categoria)
    
    def cadastrar_produto(self):
        if self.custo < 0 or self.preco_venda < 0:
            print("O custo e o preço de venda não podem ser negativos!")
            raise ValorInvalidoException("O custo e o preço de venda não podem ser negativos!")

        if self.categoria == False:
            print("A categoria informada não existe ou não foi cadastrada!")
            return False
        
        if self.descricao.strip() == "":
            print("Descrição do produto não pode ser vazio!")
            raise DescricaoEmBrancoException("Descrição do produto não pode ser vazio!")
        
        if not self.descricao.isalpha():
            print("Descrição do produto deve conter apenas letras!")
            raise ValorInvalidoException("Descrição do produto deve conter apenas letras!")
        
        if not self.codigo_barras.isnumeric():
            print("Código de barras deve conter apenas números!")
            raise ValorInvalidoException("Código de barras deve conter apenas números!")
        
        if self.fornecedor.isnumeric():
            print("Fornecedor deve conter apenas letras!")
            raise ValorInvalidoException("Fornecedor deve conter apenas letras!")
        
        if self.fornecedor.strip() == "":
            print("Fornecedor não pode ser vazio!")
            raise DescricaoEmBrancoException("Fornecedor não pode ser vazio!")
        
        if not self.categoria.isalpha():
            print("Categoria deve conter apenas letras!")
            raise ValorInvalidoException("Categoria deve conter apenas letras!")
        
        for produto in self.produtos_cadastrados:
            if produto["codigo_barras"] == self.codigo_barras:
                print(f"O produto com código de barras {self.codigo_barras} já existe!")
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

        return True

    def remover_produto(self, codigo_barras):
        for produto in self.produtos_cadastrados:
            if produto["codigo_barras"] == codigo_barras:
                self.produtos_cadastrados.remove(produto)
                print(f"Produto com código de barras {codigo_barras} removido com sucesso.")
                return True
        print(f"Produto com código de barras {codigo_barras} não encontrado.")
        return False

    def editar_produto(self, codigo_barras, novos_dados):
        for produto in self.produtos_cadastrados:
            if produto["codigo_barras"] == codigo_barras:

                if novos_dados["custo"] < 0 or novos_dados["preco_venda"] < 0:
                    print("O custo e o preço de venda não podem ser negativos!")
                    raise ValorInvalidoException("O custo e o preço de venda não podem ser negativos!")
                
                if novos_dados["descricao"].strip() == "":
                    print("Descrição do produto não pode ser vazio!")
                    raise DescricaoEmBrancoException("Descrição do produto não pode ser vazio!")
                
                if not novos_dados["descricao"].isalpha():
                    print("Descrição do produto deve conter apenas letras!")
                    raise ValorInvalidoException("Descrição do produto deve conter apenas letras!")
                
                if not novos_dados["codigo_barras"].isnumeric():
                    print("Código de barras deve conter apenas números!")
                    raise ValorInvalidoException("Código de barras deve conter apenas números!")
                
                if novos_dados["fornecedor"].isnumeric():
                    print("Fornecedor deve conter apenas letras!")
                    raise ValorInvalidoException("Fornecedor deve conter apenas letras!")
                
                if novos_dados["fornecedor"].strip() == "":
                    print("Fornecedor não pode ser vazio!")
                    raise DescricaoEmBrancoException("Fornecedor não pode ser vazio!")
                
                if not novos_dados["categoria"].isalpha():
                    print("Categoria deve conter apenas letras!")
                    raise ValorInvalidoException("Categoria deve conter apenas letras!")
                
                produto.update(novos_dados)
                print(f"Produto com código de barras {codigo_barras} editado com sucesso.")
                return True
            
        print(f"Produto com código de barras {codigo_barras} não encontrado.")
        return False


if __name__ == '__main__':
    pass

