import sys
import unittest

sys.path.append('../Models')
from Exceptions import *
from Produto import Produto
from Estoque import Estoque


class TestEstoque(unittest.TestCase):
    def setUp(self):
        self.produto = Produto("Produto Teste", "123456789", 10.0, 20.0, "Fornecedor Teste", "Categoria Teste")
        self.estoque = Estoque(self.produto, 10, "2022-01-01", "2022-01-31", "entrada")

    def test_cadastrar_estoque(self):
        self.estoque.cadastrar_estoque()
        self.assertEqual(len(self.estoque.estoque_cadastrado), 1)
        
    def test_verificar_estoque(self):
        quantity = self.estoque.verificar_estoque("123456789")
        self.assertTrue(isinstance(quantity, int))

    def test_remover_estoque(self):
        initial_quantity = self.estoque.verificar_estoque("123456789")
        qnt_remover = 2
        self.estoque.remover_estoque("123456789", qnt_remover)
        final_quantity = self.estoque.verificar_estoque("123456789")
        self.assertEqual(final_quantity, initial_quantity - qnt_remover)
        if qnt_remover >= initial_quantity:
            self.assertNotIn("123456789", [estoque["produto"].codigo_barras for estoque in self.estoque.estoque_cadastrado])

    def test_remover_estoque_com_exception(self):
        qnt_remover = 50
        self.produto = Produto("Produto Teste", "123456789", 10.0, 20.0, "Fornecedor Teste", "Categoria Teste")
        self.estoque = Estoque(self.produto, 10, "2022-01-01", "2022-01-31", "entrada")
        self.estoque.cadastrar_estoque()  # Adicione esta linha
        with self.assertRaises(EstoqueNegativoException) as context:
            self.estoque.remover_estoque("123456789", qnt_remover)
        self.assertEqual(str(context.exception), f"Estoque do produto com código de barras 123456789 não pode ser negativo.")

        final_quantity = self.estoque.verificar_estoque("123456789")
        self.assertEqual(final_quantity, 0)

    def test_editar_estoque(self):
        self.estoque.editar_estoque("123456789", {"qnt_produto": 20})
        self.assertEqual(self.estoque.estoque_cadastrado[0]["qnt_produto"], 20)
        
if __name__ == '__main__':
    unittest.main()