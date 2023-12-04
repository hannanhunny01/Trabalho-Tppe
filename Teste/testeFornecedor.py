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
        fornecedor = Fornecedor(nome="Indústrias Stark")
        self.assertFalse(fornecedor.cadastrar_fornecedor())


if __name__ == '__main__':
    unittest.main()
