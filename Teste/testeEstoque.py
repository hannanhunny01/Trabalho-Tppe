import sys
import unittest
sys.path.append('Models')
from Produto import Produto
from Estoque import Estoque

class TestEstoque(unittest.TestCase):
    def setUp(self):
        self.produto = Produto("Produto Teste", "123456789", 10.0, 20.0, "Fornecedor Teste", "Categoria Teste")
        

    def test_cadastrar_estoque(self):
        self.estoque = Estoque(self.produto, 10, "2022-01-01", "2022-01-31", "entrada")
        self.estoque2 = Estoque(self.produto, 10, "2022-01-01", "2022-01-31", "entrada")
        self.estoque3 = Estoque(self.produto, 10, "2022-01-01", "2022-01-31", "entrada")
        self.estoque.cadastrar_estoque()
        self.estoque2.cadastrar_estoque()
        self.estoque3.cadastrar_estoque()
        self.assertEqual(len(self.estoque.estoque_cadastrado), 3)
        
    def test_verificar_estoque(self):
        self.estoque = Estoque(self.produto, 10, "2022-01-01", "2022-01-31", "entrada")
        self.estoque.cadastrar_estoque()
        quantity = self.estoque.verificar_estoque("123456789")
        self.assertEqual(quantity, 10)

if __name__ == '__main__':
    unittest.main()