from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
from animals.models import Animal

"""Testes funcionais"""


class AnimalsTestCase(LiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(os.path.abspath('chromedriver'))
        self.animal = Animal.objects.create(
            name='Leão',
            predador=True,
            poisonous=False,
            domestic=False,
        )

    def tearDown(self) -> None:
        self.browser.quit()

    def test_when_user_searches_for_lion_it_returns_all_animals_with_the_word_lion(self):
        """ Teste se um usuário encontra um animal pesquisando"""

        # usuário acessa a home da aplicação Busca Animal
        self.browser.get(self.live_server_url + '/')

        # usuário encontra campo para pesquisar animais pelo nome
        doc_element = self.browser.find_element(By.CSS_SELECTOR, 'input#buscar-animal')
        self.assertEqual(doc_element.get_attribute('placeholder'), 'Exemplo: leão, urso...')

        # usuário pesquisa por Leão e clica no botão pesquisar
        doc_element.send_keys("Leão")

        self.browser.find_element(By.CSS_SELECTOR, 'form button').click()

        # site exibe 4 características do animal pesquisado

        feuture = self.browser.find_elements(By.CSS_SELECTOR, 'h3.result-description')
        print(len(feuture))
        self.assertGreater(len(feuture), 3)
