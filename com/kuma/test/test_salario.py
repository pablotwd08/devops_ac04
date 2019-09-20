from unittest import TestCase
from com.kuma.salario import salario

class TestSalario(TestCase):

	def setUp(self):
		self.salario = salario()
		
	def test_aumento(self):
		self.assertEqual(self.salario.aumento(600,25),150, "deveria ser 150")