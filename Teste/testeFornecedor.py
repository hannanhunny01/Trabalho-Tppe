import sys
import unittest

from Fornecedor import Fornecedor


sys.path.append('../Models')


class TestFornecedor(unittest.TestCase):

    def test_init_fornecedor(self):
        fornecedor = Fornecedor(nome="Indústrias Stark")
        fornecedor1 = Fornecedor(nome="LexCorp")
        fornecedor2 = Fornecedor(nome="Starlab")

        self.assertEqual(fornecedor.nome, "Indústrias Stark")
        self.assertEqual(fornecedor1.nome, "LexCorp")
        self.assertEqual(fornecedor2.nome, "Starlab")

    def test_cadastrar_fornecedor(self):
        fornecedor = Fornecedor(nome="      ")
        fornecedor1 = Fornecedor(nome="Indústrias Stark")
        fornecedor2 = Fornecedor(nome="LexCorp")

        self.assertFalse(fornecedor.cadastrar_fornecedor())
        self.assertFalse(fornecedor1.cadastrar_fornecedor())
        self.assertFalse(fornecedor2.cadastrar_fornecedor())

        self.assertEqual(len(Fornecedor.fornecedores_cadastrados), 2)
        self.assertEqual(Fornecedor.fornecedores_cadastrados[0].nome, "Indústrias Stark")
        self.assertEqual(Fornecedor.fornecedores_cadastrados[1].nome, "LexCorp")

    def test_remover_fornecedor(self):
        fornecedor = Fornecedor(nome="Indústrias Stark")
        self.assertTrue(fornecedor.remover_fornecedor()) 

        fornecedor = Fornecedor(nome="Starlab")
        self.assertFalse(fornecedor.remover_fornecedor()) 


if __name__ == '__main__':
    unittest.main()
