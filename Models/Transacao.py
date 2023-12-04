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

        self.transacoes_gravadas.append(transacao)
        print("Transacao realizado com sucesso!")

        

if __name__ == '__main__':
    pass