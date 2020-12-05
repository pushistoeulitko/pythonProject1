import allure
from selenium.webdriver.common.action_chains import ActionChains
from features.steps.brower_setting import Browser
from features.steps.Locators import Locators
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, InvalidSelectorException


class Methods(Browser):

    def open_main_page(self):
        self.driver.get('https://ru.investing.com')
        print("Зашли на сайт " + self.driver.current_url)
        assert self.driver.current_url == 'https://ru.investing.com/'

    def spam(self):
        path = Locators.LOCATOR_SPAM
        if self.driver.find_element_by_xpath(path).is_displayed():
            self.driver.find_element_by_xpath(path).click()

    def screenshots(self):
        allure.attach(self.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    def move_mouse_to_element(self, path):

        try:
            element1 = self.driver.find_element_by_xpath(path)  # Котировки
            hover = ActionChains(self.driver).move_to_element(element1)
            hover.perform()
        except Exception as e:
            print(f"Элемент отсутствует по Xpath {path}", format(e))
        else:
            print(f"Элемент присутствует по Xpath {path}")

    def click_element(self, path):
        try:
            self.driver.find_element_by_xpath(path).click()
        except Exception() as e:
            print(f"Элемент отсутствует по Xpath {path}", format(e))
        else:
            print(f"Элемент присутствует по Xpath {path}")

    def type_text(self, path, messege):
        try:
            field = self.driver.find_element_by_xpath(path)
            field.send_keys(messege)
        except Exception as e:
            print(f"Текст {messege} не передан по Xpath {path}", format(e))
        else:
            print(f"Текст {messege} передан по Xpath {path}")

    #def get_text(self, path):
        #global text0
        #try:
            #text0 = self.driver.find_element_by_xpath(path).text
        #except Exception as e:
            #print(f"Текст {text0} извлечен из элемента по Xpath {path}", format(e))
            #return text0
       # else:
            #print(f"Текст не извлечен из элемента по Xpath {path}")

    def check_word(self, path, word):
        try:
            word_0 = self.driver.find_element_by_xpath(path).text
            assert word in word_0
        except Exception as e:
            print(f"Текст {word}  отсутствует по Xpath {path}", format(e))
        else:
            print(f"Текст {word} присутствует по Xpath {path}")

    def check_elements(self, path):
        try:
            elements = self.driver.find_elements_by_xpath(path)
            number = str(len(elements))
        except Exception as e:
            print(f"Элементы не найдены {path}", format(e))
        else:
            print(f"Найдено элементов: {number}")
            return elements
