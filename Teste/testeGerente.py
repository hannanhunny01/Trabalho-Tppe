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

if __name__ == '__main__':
    unittest.main()
