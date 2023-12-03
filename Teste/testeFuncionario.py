
# test_funcionario.py


import sys 
sys.path.append('Models')
from User import Funcionario
import unittest

class TestFuncionario(unittest.TestCase):
    def test_init(self):
        funcionario = Funcionario("Maria", "111111111", "maria@email.com", "senhaabc", "555555555", "Loja C")
        self.assertEqual(funcionario.nome, "Maria")
        self.assertEqual(funcionario.telefone, "111111111")
        self.assertEqual(funcionario.email, "maria@email.com")
        self.assertEqual(funcionario.senha, "senhaabc")
        self.assertEqual(funcionario.cpf, "555555555")
        self.assertEqual(funcionario.loja, "Loja C")

    def test_exibir_informacoes_funcionario(self):
        funcionario = Funcionario("Maria", "111111111", "maria@email.com", "senhaabc", "555555555", "Loja C")
        self.assertEqual(funcionario.exibir_informacoes_funcionario(), "Nome: Maria\nTelefone: 111111111\nEmail: maria@email.com\nCPF: 555555555\nLoja: Loja C")

if __name__ == '__main__':
    unittest.main()
