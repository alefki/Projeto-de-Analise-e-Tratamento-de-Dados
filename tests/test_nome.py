import unittest
from src.services.nome import NomeService

class TestNome(unittest.TestCase):
    def setUp(self):
        self.nome_service = NomeService()

    def test_extrair_primeiro_e_segundo_nome_comum(self):
        primeiro, segundo = self.nome_service.extrair_primeiro_e_segundo_nome("Joao da Silva")
        self.assertEqual(primeiro, "Joao")
        self.assertEqual(segundo, "da")

    def test_extrair_primeiro_e_segundo_nome_composto(self):
        primeiro, segundo = self.nome_service.extrair_primeiro_e_segundo_nome("Ana dos Santos e Silva")
        self.assertEqual(primeiro, "Ana")
        self.assertEqual(segundo, "dos")

    def test_extrair_apenas_um_nome(self):
        primeiro, segundo = self.nome_service.extrair_primeiro_e_segundo_nome("Roberto")
        self.assertEqual(primeiro, "Roberto")
        self.assertEqual(segundo, "")

    def test_determinar_genero_masculino(self):
        self.assertEqual(self.nome_service.determinar_genero("Michael"), "male")

    def test_determinar_genero_feminino(self):
        self.nome_service.gender_cache = {} 
        self.assertEqual(self.nome_service.determinar_genero("Maria"), "female")

    def test_determinar_genero_nome_vazio(self):
        self.assertEqual(self.nome_service.determinar_genero(""), "unknown")

if __name__ == '__main__':
    unittest.main()

    