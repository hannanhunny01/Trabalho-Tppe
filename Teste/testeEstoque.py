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
        self.estoque = Estoque(self.produto, 8, "2022-01-01", "2022-01-31", "entrada")
        self.estoque.cadastrar_estoque()
        quantity = self.estoque.verificar_estoque("123456789")
        self.assertEqual(quantity, 8)

    def test_remover_estoque(self):
        self.estoque = Estoque(self.produto, 10, "2022-01-01", "2022-01-31", "entrada")
        self.estoque.cadastrar_estoque()
        initial_quantity = self.estoque.verificar_estoque("123456789")
        qnt_remover = 2
        self.estoque.remover_estoque("123456789", qnt_remover)
        final_quantity = self.estoque.verificar_estoque("123456789")
        self.assertEqual(final_quantity, initial_quantity - qnt_remover)
        if qnt_remover >= initial_quantity:
            self.assertNotIn("123456789", [estoque["produto"].codigo_barras for estoque in self.estoque.estoque_cadastrado])

if __name__ == '__main__':
    unittest.main()