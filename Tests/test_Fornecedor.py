import unittest
from parameterized import parameterized
import sys
sys.path.append('../Models')
from Fornecedor import Fornecedor

class TestFornecedor(unittest.TestCase):

    @parameterized.expand([
        ("Indústrias Stark", "Minesota, EUA", "001", "123456789", "Indústrias Stark", "Minesota, EUA", "001", "123456789"),
        ("StarLab", "Califórnia, EUA", "002", "987654321", "StarLab", "Califórnia, EUA", "002", "987654321"),
    ])
    def test_init(self, nome1, endereco1, codigo1, telefone1, nome2, endereco2, codigo2, telefone2):
        fornecedor1 = Fornecedor(nome=nome1, endereco=endereco1, codigo_fornecedor=codigo1, telefone=telefone1)
        fornecedor2 = Fornecedor(nome=nome2, endereco=endereco2, codigo_fornecedor=codigo2, telefone=telefone2)

        self.assertEqual(fornecedor1.nome, nome1)
        self.assertEqual(fornecedor1.endereco, endereco1)
        self.assertEqual(fornecedor1.codigo_fornecedor, codigo1)
        self.assertEqual(fornecedor1.telefone, telefone1)

        self.assertEqual(fornecedor2.nome, nome2)
        self.assertEqual(fornecedor2.endereco, endereco2)
        self.assertEqual(fornecedor2.codigo_fornecedor, codigo2)
        self.assertEqual(fornecedor2.telefone, telefone2)

    @parameterized.expand([
        ("Indústrias Stark", "Minesota, EUA", "001", "aaaaaa", False),
        ("StarLab", "Califórnia, EUA", "002", "5551234567", True),
    ])
    def test_cadastrar_fornecedor(self, nome, endereco, codigo, telefone, resultado_esperado):
        fornecedor = Fornecedor(nome=nome, endereco=endereco, codigo_fornecedor=codigo, telefone=telefone)
        self.assertEqual(fornecedor.cadastrar_fornecedor(), resultado_esperado)

        if resultado_esperado:
            self.assertEqual(len(Fornecedor.fornecedores_cadastrados), 1)
            self.assertEqual(Fornecedor.fornecedores_cadastrados[0]['nome'], nome)
            self.assertEqual(Fornecedor.fornecedores_cadastrados[0]['endereco'], endereco)
            self.assertEqual(Fornecedor.fornecedores_cadastrados[0]['codigo_fornecedor'], codigo)
            self.assertEqual(Fornecedor.fornecedores_cadastrados[0]['telefone'], telefone)

    @parameterized.expand([
        ("001", 1),
        ("002", 1),
    ])
    def test_remover_fornecedor(self, codigo, num_fornecedores_restantes):
        fornecedor = Fornecedor(nome="Indústrias Stark", endereco="Minesota, EUA", codigo_fornecedor=codigo, telefone="123456789")
        fornecedor.cadastrar_fornecedor()

        fornecedor.remover_fornecedor(codigo)
        self.assertEqual(len(Fornecedor.fornecedores_cadastrados), num_fornecedores_restantes)

    @parameterized.expand([
        ("002", {"nome": "LexCorp"}, True),
        ("007", {"nome": "LexCorp", "endereco": "Ohio, EUA", "codigo_fornecedor": "007", "telefone": "789456132"}, False),
    ])
    def test_editar_fornecedor(self, codigo, dados, resultado_esperado):
        fornecedor = Fornecedor(nome="Indústrias Cleiton", endereco="New York, EUA", codigo_fornecedor="003", telefone="2613225233")

        self.assertEqual(fornecedor.editar_fornecedor(codigo, dados), resultado_esperado)

if __name__ == '__main__':
    unittest.main()
