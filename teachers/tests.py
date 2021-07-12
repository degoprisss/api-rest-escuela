from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from teachers.models import Teachers


class TeacherApiTest(APITestCase):

    def setUp(self) :
        Teachers.objects.create(
            first_name= "Diego 2",
            last_name= "Mesa Luna",
            age= "23",
            email= "degoprisss@gmail.com",
            phone= "3105523237"
        )

    def test_create_libro(self):
        #autor = Teachers.objects.create(nombre='Diego', email='diego@gmail.com', fecha_publicacion='2021-01-01')
        data = {
                "first_name": "Diego 2",
                "last_name": "Mesa Luna",
                "age": "23",
                "email": "degoprisss@gmail.com",
                "phone": "3105523237"
        }

        response = self.client.post('http://127.0.0.1:8000/teachers/', data=data)
        self.assertEqual(response.status_code, 201)
        self.assertNotEqual(len(response.data), 0)

    def test_get_teacher(self):
        response = self.client.get('http://127.0.0.1:8000/teachers/')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_update_libro(self):
        data = {
            "first_name": "Diego 6"
        }

        response = self.client.patch('http://127.0.0.1:8000/teachers/1/')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)


