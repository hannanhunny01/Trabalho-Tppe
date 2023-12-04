import sys
import unittest

from Fornecedor import Fornecedor


sys.path.append('../Models')


class TestFornecedor(unittest.TestCase):

    def test_init_fornecedor(self):
        fornecedor = Fornecedor(nome="Indústrias Stark")

        self.assertEqual(fornecedor.nome, "Indústrias Stark")


if __name__ == '__main__':
    unittest.main()
