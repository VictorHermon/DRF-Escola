from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status


class CursoTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso(
            codigo_curso='CTT1', descricao='Curso de Teste 01', nivel='B'
        )
        self.curso_2 = Curso(
            codigo_curso='CTT2', descricao='Curso de Teste 02', nivel='A'
        )

    # def test_falhador(self):
    #     self.fail('Teste falhou de proósito')

    def test_requisicao_get_para_listar_cursos(self):
        """Teste para verificar a requisição GET para listar os cursos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_curso(self):
        """Teste para verificar a requisição POST para criar um curso"""
        data = {
            'codigo_curso': 'CTT3',
            'descricao': 'Curso de Teste 03',
            'nivel': 'A'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
