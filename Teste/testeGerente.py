import unittest
import sys 
sys.path.append('Models')
from User import Gerente



class TestGerente(unittest.TestCase):
    def test_init(self):
        gerente = Gerente("João", "987654321", "joao@email.com", "senha456", "123456789", ["Loja A", "Loja B"])
        self.assertEqual(gerente.nome, "João")
        self.assertEqual(gerente.telefone, "987654321")
        self.assertEqual(gerente.email, "joao@email.com")
        self.assertEqual(gerente.senha, "senha456")
        self.assertEqual(gerente.cpf, "123456789")
        self.assertEqual(gerente.lojas, ["Loja A", "Loja B"])

    def test_exibir_informacoes_gerente(self):
        gerente = Gerente("João", "987654321", "joao@email.com", "senha456", "123456789", ["Loja A", "Loja B"])
        self.assertEqual(gerente.exibir_informacoes_gerente(), "Nome: João\nTelefone: 987654321\nEmail: joao@email.com\nCPF: 123456789\nLojas: Loja A, Loja B")

    def test_listar_gerentes(self):
        gerentes = [Gerente("Gerente1", "123456789", "gerente1@example.com", "senha123", "12345678901", ["Loja1", "Loja2"])]
        self.assertEqual(Gerente.listar_gerentes(gerentes), gerentes)

    def test_salvar_gerente(self):
        gerentes = []
        gerente = Gerente("Gerente1", "123456789", "gerente1@example.com", "senha123", "12345678901", ["Loja1", "Loja2"])
        gerentes = gerente.salvar_gerente(gerentes)
        self.assertEqual(len(gerentes), 1)

    def test_atualizar_gerente(self):
        gerentes = [Gerente("Gerente1", "123456789", "gerente1@example.com", "senha123", "12345678901", ["Loja1", "Loja2"])]
        novo_gerente = Gerente("Gerente1", "123456789", "gerente1@example.com", "senha456", "12345678901", ["Loja3"])
        gerentes = novo_gerente.atualizar_gerente(gerentes)
        self.assertEqual(gerentes[0].senha, "senha456")

    def test_excluir_gerente(self):
        gerentes = [Gerente("Gerente1", "123456789", "gerente1@example.com", "senha123", "12345678901", ["Loja1", "Loja2"])]
        email = "gerente1@example.com"
        gerentes = Gerente.excluir_gerente(email, gerentes)
        self.assertEqual(len(gerentes), 0)

if __name__ == '__main__':
    unittest.main()
