
# test_funcionario.py


import sys 
sys.path.append('../Models')
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
    
    def test_listar_funcionarios(self):
        funcionarios = [Funcionario("Funcionario1", "987654321", "funcionario1@example.com", "senha456", "98765432101", "Loja3")]
        self.assertEqual(Funcionario.listar_funcionarios(funcionarios), funcionarios)

    def test_salvar_funcionario(self):
        funcionarios = []
        funcionario = Funcionario("Funcionario1", "987654321", "funcionario1@example.com", "senha456", "98765432101", "Loja3")
        funcionarios = funcionario.salvar_funcionario(funcionarios)
        self.assertEqual(len(funcionarios), 1)

    def test_atualizar_funcionario(self):
        funcionarios = [Funcionario("Funcionario1", "987654321", "funcionario1@example.com", "senha456", "98765432101", "Loja3")]
        novo_funcionario = Funcionario("Funcionario1", "987654321", "funcionario1@example.com", "senha789", "98765432101", "Loja4")
        funcionarios = novo_funcionario.atualizar_funcionario(funcionarios)
        self.assertEqual(funcionarios[0].senha, "senha789")

    def test_excluir_funcionario(self):
        funcionarios = [Funcionario("Funcionario1", "987654321", "funcionario1@example.com", "senha456", "98765432101", "Loja3")]
        email = "funcionario1@example.com"
        funcionarios = Funcionario.excluir_funcionario(email, funcionarios)
        self.assertEqual(len(funcionarios), 0)

if __name__ == '__main__':
    unittest.main()
