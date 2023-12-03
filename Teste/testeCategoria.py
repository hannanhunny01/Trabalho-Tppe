import unittest
import sys
sys.path.append('../Models')
from Categoria import Categoria

class TestCategoria(unittest.TestCase):

    def test_init_categoria(self):
        categoria = Categoria(nome="Roupa")

        self.assertEqual(categoria.nome, "Roupa")

if __name__ == '__main__':
    unittest.main()
