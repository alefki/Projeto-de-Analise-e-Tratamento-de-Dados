import unittest
from src.services.celular import CelularService

class TestCelular(unittest.TestCase):
    def setUp(self):
        self.celular_service = CelularService()

    def test_limpar_celular_remove_formatacao(self):
        self.assertEqual(self.celular_service.limpar_celular("(11) 98765-4321"), "11987654321")
        self.assertEqual(self.celular_service.limpar_celular("55 21 912345678"), "5521912345678")
        self.assertEqual(self.celular_service.limpar_celular("1234-5678"), "12345678")
        self.assertEqual(self.celular_service.limpar_celular(""), "")
        self.assertEqual(self.celular_service.limpar_celular(None), "")
        self.assertEqual(self.celular_service.limpar_celular("abc123xyz"), "123")

    def test_celular_eh_valido_formatos_corretos(self):
        self.assertTrue(self.celular_service.eh_valido("987654321"))
        self.assertTrue(self.celular_service.eh_valido("12345678"))
        self.assertTrue(self.celular_service.eh_valido("41987654321"))
        self.assertTrue(self.celular_service.eh_valido("2112345678"))

    def test_celular_eh_valido_poucos_digitos(self):
        self.assertFalse(self.celular_service.eh_valido("123"))
        self.assertFalse(self.celular_service.eh_valido("1234567"))

    def test_celular_eh_valido_muitos_digitos(self):
        self.assertFalse(self.celular_service.eh_valido("123456789012"))

    def test_celular_eh_valido_caracteres_nao_numericos(self):
        self.assertFalse(self.celular_service.eh_valido("abcde1234"))
        self.assertFalse(self.celular_service.eh_valido("987-65x-432"))

    def test_celular_eh_valido_string_vazia(self):
        self.assertFalse(self.celular_service.eh_valido(""))

    def test_celular_eh_valido_none(self):
        self.assertFalse(self.celular_service.eh_valido(None))

if __name__ == '__main__':
    unittest.main()

    