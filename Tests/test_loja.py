import unittest
import sys
sys.path.append('../Models')
from Loja import Loja
import unittest
from parameterized import parameterized

class TestLoja(unittest.TestCase):

    @parameterized.expand([
        ("Loja1", "123456789", "Endereco1", "Representante1", [], [], True),
        ("Loja2", "987654321", "Endereco2", "Representante2", [], [], True),
        ("", "123456789", "Endereco1", "Representante1", [], [], False),
    ])
    def test_cadastrar_loja(self, nome, cnpj, endereco, representante, estoques, funcionarios, resultado_esperado):
        loja = Loja(nome, cnpj, endereco, representante, estoques, funcionarios)
        self.assertEqual(loja.cadastrar_loja(), resultado_esperado)

    @parameterized.expand([
        ("Loja1", True),
        ("Loja3", False),
    ])
    def test_remover_loja(self, nome, resultado_esperado):
        loja = Loja("Loja1", "123456789", "Endereco1", "Representante1", [], [])
        self.assertEqual(loja.remover_loja(), resultado_esperado)

    def test_listar_lojas(self):
        loja = Loja("Loja1", "123456789", "Endereco1", "Representante1", [], [])
        loja.cadastrar_loja()
        self.assertEqual(len(loja.listar_lojas()), 2)

    @parameterized.expand([
        ("Loja1", "Loja1"),
        ("Loja3", False),
    ])
    def test_obter_loja_por_nome(self, nome, resultado_esperado):
        loja = Loja("Loja1", "123456789", "Endereco1", "Representante1", [], [])
        loja.cadastrar_loja()
        self.assertEqual(loja.obter_loja_por_nome(nome), resultado_esperado)

    def test_listar_lojas(self):
        loja = Loja("Loja5", "3267252", "Endereco5", "Representante5", [], [])
        self.assertEqual(len(loja.listar_lojas()), 2)

    @parameterized.expand([
        ("123456789", {"nome": "NovaLoja", "representante": "NovoRepresentante"}, True),
        ("987654321", {"endereco": "NovoEndereco"}, True),
        ("111111111", {"estoques": ["Estoque1", "Estoque2"]}, False),
    ])
    def test_editar_loja(self, cnpj, dados, resultado_esperado):
        loja = Loja("NovaLoja", "123456789", "Endereco1", "Representante1", [], [])
        self.assertEqual(loja.editar_loja(cnpj, dados), resultado_esperado)

if __name__ == '__main__':
    unittest.main()
