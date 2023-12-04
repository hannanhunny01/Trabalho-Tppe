import unittest
from Loja import Loja

class TestLoja(unittest.TestCase):

    def test_cadastrar_loja(self):
        loja = Loja(
            nome="Loja Teste",
            cnpj="123456789",
            endereco="Rua Teste, 123",
            representante="123",
            estoques=[],
            funcionarios=[]
        )

        # Teste de cadastro bem-sucedido
        self.assertEqual(len(loja.listar_lojas()), 0)
        self.assertTrue(loja.cadastrar_loja())
        self.assertEqual(len(loja.listar_lojas()), 1)

        # Tentativa de cadastrar a mesma loja novamente
        self.assertFalse(loja.cadastrar_loja())

        # Tentativa de cadastrar uma loja com nome vazio
        loja.nome = ""
        self.assertFalse(loja.cadastrar_loja())

    def test_remover_loja(self):
        loja = Loja(
            nome="Loja Teste",
            cnpj="123456789",
            endereco="Rua Teste, 123",
            representante="123",
            estoques=[],
            funcionarios=[]
        )

        self.assertTrue(loja.remover_loja())
        self.assertEqual(len(loja.listar_lojas()), 0)

    def test_editar_loja(self):
        loja = Loja(
            nome="Loja Teste",
            cnpj="123456789",
            endereco="Rua Teste, 123",
            representante="123",
            estoques=[],
            funcionarios=[]
        )

        # Tentativa de editar uma loja que não existe
        self.assertFalse(loja.editar_loja("987654321", {"endereco": "Nova Rua, 456"}))

        # Cadastrar a loja e depois editá-la
        loja.cadastrar_loja()
        self.assertEqual(loja.listar_lojas()[0]["endereco"], "Rua Teste, 123")
        self.assertTrue(loja.editar_loja("123456789", {"endereco": "Nova Rua, 456"}))
        self.assertEqual(loja.listar_lojas()[0]["endereco"], "Nova Rua, 456")

    def test_obter_loja_por_nome(self):
        loja = Loja(
            nome="Loja Teste",
            cnpj="123456789",
            endereco="Rua Teste, 123",
            representante="123",
            estoques=[],
            funcionarios=[]
        )

        # Tentativa de obter uma loja que não existe
        self.assertFalse(loja.obter_loja_por_nome("Loja Inexistente"))

        # Cadastrar a loja e depois tentar obter por nome
        loja.cadastrar_loja()
        loja_obtida = loja.obter_loja_por_nome("Loja Teste")
        self.assertEqual(loja_obtida["nome"], "Loja Teste")

if __name__ == '__main__':
    unittest.main()
