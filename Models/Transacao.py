class Transacao:
    transacoes_gravadas = []

    def __init__(self, produto, quantidade, fornecedor, loja):
        self.produto = produto
        self.quantidade = quantidade
        self.fornecedor = fornecedor
        self.loja = loja
    
    def fazer_transacao(self):
        transacao = {
            "produto": self.produto,
            "quantidade": self.quantidade,
            "fornecedor": self.fornecedor,
            "loja": self.loja
        }

        if self.fornecedor.estoques.qnt_produto >= 0 and self.loja.estoques.qnt_produto >= 0:
            self.fornecedor.estoques.qnt_produto = self.fornecedor.estoques.qnt_produto - self.quantidade

            self.loja.estoques.qnt_produto = self.loja.estoques.qnt_produto + self.quantidade
        
        self.transacoes_gravadas.append(transacao)

        print("Transação realizada com sucesso!")
    
    def desfazer_transacao(self):
        transacao = {
            "produto": self.produto,
            "quantidade": self.quantidade,
            "fornecedor": self.fornecedor,
            "loja": self.loja
        }

        if self.fornecedor.estoques.qnt_produto >= 0 and self.loja.estoques.qnt_produto >= 0:
            self.fornecedor.estoques.qnt_produto = self.fornecedor.estoques.qnt_produto + self.quantidade

            self.loja.estoques.qnt_produto = self.loja.estoques.qnt_produto - self.quantidade
        
        self.transacoes_gravadas.append(transacao)

        print("Transação realizada com sucesso!")


if __name__ == '__main__':
    pass