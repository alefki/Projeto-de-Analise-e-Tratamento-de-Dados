import unittest
from src.services.cep import CEPService

class TestCEPService(unittest.TestCase):
    def setUp(self):
        self.cep_service = CEPService()

    def test_buscar_endereco_cep_valido(self):
        endereco = self.cep_service.buscar_endereco_por_cep("01001-000")
        self.assertIsNotNone(endereco)
        self.assertEqual(endereco['cep'], '01001-000')
        self.assertEqual(endereco['logradouro'], 'Praça da Sé')
        self.assertEqual(endereco['localidade'], 'São Paulo')
        self.assertEqual(endereco['uf'], 'SP')

    def test_buscar_endereco_cep_inexistente(self):
        endereco = self.cep_service.buscar_endereco_por_cep("99999-999")
        if endereco is not None:
            self.assertIn('erro', endereco)
            self.assertTrue(endereco['erro'])
        else:
            self.assertIsNone(endereco)

    def test_buscar_endereco_cep_invalido_formato(self):
        endereco_curto = self.cep_service.buscar_endereco_por_cep("12345")
        self.assertIsNone(endereco_curto)

        endereco_letras = self.cep_service.buscar_endereco_por_cep("abcde123")
        self.assertIsNone(endereco_letras)

        endereco_vazio = self.cep_service.buscar_endereco_por_cep("")
        self.assertIsNone(endereco_vazio)

    def test_buscar_endereco_cep_com_mascara(self):
        endereco = self.cep_service.buscar_endereco_por_cep("01001-000")
        self.assertIsNotNone(endereco)
        self.assertEqual(endereco['cep'], '01001-000')

    def test_cache_funciona(self):
        cep_para_cache = "01310-100"
        endereco_primeira_vez = self.cep_service.buscar_endereco_por_cep(cep_para_cache)
        self.assertIsNotNone(endereco_primeira_vez)
        self.assertIn("01310100", self.cep_service.cep_cache)
        self.assertEqual(self.cep_service.cep_cache["01310100"], endereco_primeira_vez)

if __name__ == '__main__':
    unittest.main()

    