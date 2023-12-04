import unittest
import sys
sys.path.append('../Models')
from Transacao import Transacao
from Produto import Produto
from Estoque import Estoque
from Loja_ex import Loja

class TestTransacao(unittest.TestCase):

    def test_init_transacao(self):
        transacao = Transacao(produto="Creatina Turbo 300g", quantidade=50, fornecedor="LTDA BodyBuilder", loja="Loja de marombas")
        transacao2 = Transacao(produto="Downy Perfume Collection Amaciante", quantidade=200, fornecedor="LTDA RoupasCheirosas", loja="Mercado Jota")

        self.assertEqual(transacao.produto, "Creatina Turbo 300g")
        self.assertEqual(transacao.quantidade, 50)
        self.assertEqual(transacao.fornecedor, "LTDA BodyBuilder")
        self.assertEqual(transacao.loja, "Loja de marombas")

        self.assertEqual(transacao2.produto, "Downy Perfume Collection Amaciante")
        self.assertEqual(transacao2.quantidade, 200)
        self.assertEqual(transacao2.fornecedor, "LTDA RoupasCheirosas")
        self.assertEqual(transacao2.loja, "Mercado Jota")

    def teste_fazer_transacao(self):
        produto1 = Produto(descricao="Creatina Turbo 300g", codigo_barras="1234567890", custo=10.0, preco_venda=27.0, fornecedor="LTDA BodyBuilder", categoria="Academia")
        estoque1 = Estoque(produto=produto1, qnt_produto=400, data_entrada="2022-01-01", data_saida="2022-01-31", tipo_transacao="saida")
        estoque2 = Estoque(produto=produto1, qnt_produto=50, data_entrada="2022-01-01", data_saida="2022-01-31", tipo_transacao="entrada")
        loja1 = Loja(nome="LTDA BodyBuilder", cnpj="23412341999223", endereco="Rua josivaldo 3, 123", representante="Gerlado fulano", estoques=estoque1, funcionarios=[])
        loja2 = Loja(nome="Loja de marombas", cnpj="12345678901234", endereco="Rua garibaldo 3, 123", representante="Gerlado fulano", estoques=estoque2, funcionarios=[])

        transacao = Transacao(produto=produto1, quantidade=50, fornecedor="LTDA BodyBuilder", loja=loja2)

        transacao.fazer_transacao()

        self.assertEqual(loja1.estoques.qnt_produto, 350)
        self.assertEqual(loja2.estoques.qnt_produto, 100)


if __name__ == '__main__':
    unittest.main()