import unittest
from src.services.cpf import CPFService

class TestCPF(unittest.TestCase):
    def setUp(self):
        self.cpf_service = CPFService()

    def test_limpar_cpf_remove_formatacao(self):
        self.assertEqual(self.cpf_service.limpar_cpf("123.456.789-00"), "12345678900")
        self.assertEqual(self.cpf_service.limpar_cpf("987-654.321/01"), "98765432101")
        self.assertEqual(self.cpf_service.limpar_cpf(""), "")
        self.assertEqual(self.cpf_service.limpar_cpf(None), "")
        self.assertEqual(self.cpf_service.limpar_cpf("abc123def"), "123")

    def test_cpf_eh_valido_com_digitos_corretos(self):
        self.assertTrue(self.cpf_service.eh_valido("111.444.777-05"))
        self.assertTrue(self.cpf_service.eh_valido("000.000.000-00"))
        self.assertTrue(self.cpf_service.eh_valido("12345678900"))
        self.assertTrue(self.cpf_service.eh_valido("94097729828"))

    def test_cpf_eh_valido_com_digitos_iguais(self):
        self.assertFalse(self.cpf_service.eh_valido("11111111111"))
        self.assertFalse(self.cpf_service.eh_valido("22222222222"))
        self.assertFalse(self.cpf_service.eh_valido("00000000000"))

    def test_cpf_invalido_com_tamanho_errado(self):
        self.assertFalse(self.cpf_service.eh_valido("12345678"))
        self.assertFalse(self.cpf_service.eh_valido("123456789012"))
        self.assertFalse(self.cpf_service.eh_valido(""))

    def test_cpf_invalido_com_digitos_verificadores_incorretos(self):
        self.assertFalse(self.cpf_service.eh_valido("12345678901"))
        self.assertFalse(self.cpf_service.eh_valido("94097729829"))
        self.assertFalse(self.cpf_service.eh_valido("77982063131")) 

if __name__ == '__main__':
    unittest.main()

