import sys
import unittest

from Fornecedor import Fornecedor


sys.path.append('../Models')


class TestFornecedor(unittest.TestCase):

    def test_init_produto(self):
        fornecedor1 = Fornecedor("Indústrias Stark", "Minesota, EUA", "001", "123456789")
        fornecedor2 = Fornecedor("StarLab", "Califórnia, EUA", "002", "987654321")
        
        fornecedor1.cadastrar_fornecedor()
        fornecedor2.cadastrar_fornecedor()

        self.assertEqual(fornecedor1.nome, "Indústrias Stark")
        self.assertEqual(fornecedor1.endereco, "Minesota, EUA")
        self.assertEqual(fornecedor1.codigo_fornecedor, "001")
        self.assertEqual(fornecedor1.telefone, "123456789")

        self.assertEqual(fornecedor2.nome, "StarLab")
        self.assertEqual(fornecedor2.endereco, "Califórnia, EUA")
        self.assertEqual(fornecedor2.codigo_fornecedor, "002")
        self.assertEqual(fornecedor2.telefone, "987654321")

    def test_cadastrar_fornecedor(self):
        fornecedor1 = Fornecedor(nome="Indústrias Stark", endereco="Minesota, EUA", codigo_fornecedor="001", telefone="aaaaaa")
        fornecedor2 = Fornecedor(nome="StarLab", endereco="Califórnia, EUA", codigo_fornecedor="002", telefone="987654321")
        self.assertFalse(fornecedor1.cadastrar_produto())
        self.assertTrue(fornecedor2.cadastrar_produto())

        self.assertEqual(len(Fornecedor.fornecedores_cadastrados), 1)
        self.assertEqual(Fornecedor.fornecedores_cadastrados[0].nome, "StarLab")
        self.assertEqual(Fornecedor.fornecedores_cadastrados[0].endereco, "Califórnia, EUA")
        self.assertEqual(Fornecedor.fornecedores_cadastrados[0].codigo_fornecedor, "002")
        self.assertEqual(Fornecedor.fornecedores_cadastrados[0].telefone, "987654321")

    def test_remover_fornecedor(self):
        fornecedor1 = Fornecedor(nome="Indústrias Stark", endereco="Minesota, EUA", codigo_fornecedor="001", telefone="123456789")
        fornecedor2 = Fornecedor(nome="StarLab", endereco="Califórnia, EUA", codigo_fornecedor="002", telefone="987654321")
        
        Fornecedor.remover_fornecedor("002")

        self.assertEqual(len(Fornecedor.fornecedores_cadastrados), 1)

        self.assertEqual(Fornecedor.fornecedores_cadastrados[0].nome, fornecedor1)

    def test_editar_fornecedor(self):
        fornecedor = Fornecedor(nome="Indústrias Stark", endereco="Minesota, EUA", codigo_fornecedor="001", telefone="123456789")
        fornecedor.cadastrar_fornecedor()

        self.assertTrue(fornecedor.editar_fornecedor("001", {"nome": "LexCorp", "endereco": "Ohio, EUA", "codigo_fornecedor": "001", "telefone": "789456132"}))
        
        self.assertFalse(fornecedor.editar_fornecedor("007", {"nome": "LexCorp", "endereco": "Ohio, EUA", "codigo_fornecedor": "007", "telefone": "789456132"}))


if __name__ == '__main__':
    unittest.main()
