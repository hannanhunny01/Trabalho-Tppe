from Loja import Loja
import sys
import unittest
sys.path.append('../Models')


class TestLoja(unittest.TestCase):

    def setUp(self):
        self.loja = Loja("Loja Teste", "123456789",
                         "Rua Teste, 123", "Representante Teste", [], [])

    def test_cadastrar_loja(self):
        self.assertEqual(len(self.loja.lojas_cadastradas), 1)

    def test_remover_loja(self):
        self.loja.remover_loja("123456789")
        self.assertEqual(len(self.loja.lojas_cadastradas), 0)

    def test_editar_loja(self):
        self.loja.editar_loja("123456789", {"nome": "Loja Teste 2"})
        self.assertEqual(
            self.loja.lojas_cadastradas[0]["nome"], "Loja Teste 2")

    def test_listar_lojas(self):
        self.assertEqual(self.loja.listar_lojas(), self.loja.lojas_cadastradas)

    def test_buscar_loja_nome(self):
        self.assertEqual(self.loja.buscar_loja_nome(
            "Loja Teste"), self.loja.lojas_cadastradas[0])

    def test_associar_funcionario(self):
        self.loja.cadastrar_loja()
        self.loja.associar_funcionario("123456789")
        self.assertEqual(self.loja.lojas_cadastradas[0]["funcionarios"], ["123456789"])

    def test_desassociar_funcionario(self):
        self.loja.desassociar_funcionario("123456789")
        self.assertEqual(self.loja.lojas_cadastradas[0]["funcionarios"], [])

    def test_associar_representante(self):
        self.loja.associar_representante("123456789")
        self.assertEqual(self.loja.lojas_cadastradas[0]["representante"], "123456789")


if __name__ == '__main__':
    unittest.main()
