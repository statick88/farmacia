from rest_framework.test import APITestCase
from rest_framework import status
from .models import Medicamento


class MedicamentoAPITests(APITestCase):
    def setUp(self):
        self.medicamento = Medicamento.objects.create(
            nombre="Paracetamol",
            precio=10,
            existencias=50,
            lugar="Almacén A"
        )

    def test_lista_medicamentos(self):
        response = self.client.get('/api/medicamentos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


def test_crear_medicamento(self):
    data = {
        "nombre": "Ibuprofeno",
        "precio": 15,
        "existencias": 30,
        "lugar": "Almacén B"
    }
    response = self.client.post('/api/medicamentos/', data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(response.data['nombre'], data['nombre'])
    self.assertEqual(response.data['precio'], data['precio'])
    self.assertEqual(response.data['existencias'], data['existencias'])
    self.assertEqual(response.data['lugar'], data['lugar'])

    def test_detalle_medicamento(self):
        response = self.client.get(f'/api/medicamentos/{self.medicamento.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], "Paracetamol")
