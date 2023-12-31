from Exceptions import *
class Estoque:
    estoque_cadastrado = []

    def __init__(self, produto, qnt_produto, data_entrada, data_saida, tipo_transacao):
        self.produto = produto
        self.qnt_produto = qnt_produto
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.tipo_transacao = tipo_transacao

    def cadastrar_estoque(self):
        estoque_info = {
            "Produto": self.produto,
            "Quantidade": self.qnt_produto,
            "Data de Entrada": self.data_entrada,
            "Data de Saída": self.data_saida,
            "Tipo de Transação": self.tipo_transacao
        }
        self.estoque_cadastrado.append(estoque_info)

    def verificar_estoque(self, codigo_barras):
        for estoque in self.estoque_cadastrado:
            if estoque["Produto"].codigo_barras == codigo_barras:
                return estoque["Quantidade"]
        raise CodigoDeBarrasException(f"Produto com código de barras {codigo_barras} não encontrado no estoque.")

    def remover_estoque(self, codigo_barras, qnt_remover):
        for estoque in self.estoque_cadastrado:
            if estoque["Produto"].codigo_barras == codigo_barras:
                estoque["Quantidade"] -= qnt_remover
                if estoque["Quantidade"] < 0:
                    estoque["Quantidade"] = 0
                    raise EstoqueNegativoException(f"Estoque do produto com código de barras {codigo_barras} não pode ser negativo.")
                if estoque["Quantidade"] == 0:
                    self.estoque_cadastrado.remove(estoque)
                break
        else:
            raise CodigoDeBarrasException(f"Produto com código de barras {codigo_barras} não encontrado no estoque.")
    def editar_estoque(self, codigo_barras, novos_dados):
        for estoque in self.estoque_cadastrado:
            if estoque["Produto"].codigo_barras == codigo_barras:
                estoque.update(novos_dados)
                break
        else:
            raise CodigoDeBarrasException(f"Produto com código de barras {codigo_barras} não encontrado no estoque.")