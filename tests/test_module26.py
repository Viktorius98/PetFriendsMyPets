from pages.auth_page import AuthPage
import time


def test_auth_page(selenium):
   page = AuthPage(selenium)
   page.enter_email("viksin376@yandex.ru")
   page.enter_pass("Rkb[Ntc23")
   page.btn_click()

   #знак != или == будет зависеть от того, верные или неверные данные мы вводим
    assert page.get_relative_link() != '/all_pets', "login error"

   time.sleep(5) #задержка для учебных целей