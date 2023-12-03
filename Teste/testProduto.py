import unittest
import sys
sys.path.append('../Models')
from Produto import Produto

class TestProduto(unittest.TestCase):

    def test_init_produto(self):
        produto = Produto(descricao="Camiseta", codigo_barras="1234567890", custo=10.0, preco_venda=20.0, fornecedor="Fornecedor A", categoria="Roupa")
        produto2 = Produto(descricao="Arroz", codigo_barras="0987654321", custo=15.0, preco_venda=25.0, fornecedor="Fornecedor B", categoria="Alimento")

        self.assertEqual(produto.descricao, "Camiseta")
        self.assertEqual(produto.codigo_barras, "1234567890")
        self.assertEqual(produto.custo, 10.0)
        self.assertEqual(produto.preco_venda, 20.0)
        self.assertEqual(produto.fornecedor, "Fornecedor A")
        self.assertEqual(produto.categoria, "Roupa")

        self.assertEqual(produto2.descricao, "Arroz")
        self.assertEqual(produto2.codigo_barras, "0987654321")
        self.assertEqual(produto2.custo, 15.0)
        self.assertEqual(produto2.preco_venda, 25.0)
        self.assertEqual(produto2.fornecedor, "Fornecedor B")
        self.assertEqual(produto2.categoria, "Alimento")

    def test_cadastrar_produto(self):
        produto = Produto(descricao="Coxinha", codigo_barras="712736221", custo=10.0, preco_venda=20.0, fornecedor="Fornecedor A", categoria="Alimento")
        produto2 = Produto(descricao="Camiseta", codigo_barras="1234567890", custo=-10.0, preco_venda=20.0, fornecedor="Fornecedor A", categoria="Roupa")
        self.assertFalse(produto.cadastrar_produto())
        self.assertFalse(produto2.cadastrar_produto())

    def test_remover_produto(self):
        produto = Produto(descricao="Carro", codigo_barras="1234567890", custo=10.0, preco_venda=20.0, fornecedor="Fornecedor B", categoria="Automovel")
        self.assertFalse(produto.remover_produto("1234567890"))


if __name__ == '__main__':
    unittest.main()