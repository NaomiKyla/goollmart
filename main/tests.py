from django.test import TestCase, Client

class MainViewTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/')
        self.assertTemplateUsed(response, 'main.html')  # sesuai path template kamu

    def test_context_data(self):
        response = Client().get('/')
        self.assertContains(response, "GoollMart")  
        self.assertContains(response, "2406434102")  # NPM kamu
        self.assertContains(response, "Naomi Kyla Zahra Siregar")  # Nama kamu
        self.assertContains(response, "PBP B")  # Kelas kamu
