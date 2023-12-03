import unittest
import sys
sys.path.append('../Models')
from Transacao import Transacao

class TestTransacao(unittest.TestCase):

    def test_init_transacao(self):
        transacao = Transacao(produto="Creatina Turbo 300g", quantidade=50, fornecedor="LTDA BodyBuilder", loja="Loja de marombas")

        self.assertEqual(transacao.produto, "Creatina Turbo 300g")
        self.assertEqual(transacao.quantidade, 50)
        self.assertEqual(transacao.fornecedor, "LTDA BodyBuilder")
        self.assertEqual(transacao.loja, "Loja de marombas")

if __name__ == '__main__':
    unittest.main()