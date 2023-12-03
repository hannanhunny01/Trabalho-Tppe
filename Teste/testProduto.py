import unittest
import sys
sys.path.append('../Models')
from Produto import Produto

class TestProduto(unittest.TestCase):

    def test_init_produto(self):
        produto = Produto(descricao="Camiseta", codigo_barras="1234567890", custo=10.0, preco_venda=20.0, fornecedor="Fornecedor A", categoria="Roupa")

        self.assertEqual(produto.descricao, "Camiseta")
        self.assertEqual(produto.codigo_barras, "1234567890")
        self.assertEqual(produto.custo, 10.0)
        self.assertEqual(produto.preco_venda, 20.0)
        self.assertEqual(produto.fornecedor, "Fornecedor A")
        self.assertEqual(produto.categoria, "Roupa")

if __name__ == '__main__':
    unittest.main()