import allure
from selenium.webdriver.common.action_chains import ActionChains
from features.steps.brower_setting import Browser
from features.steps.Locators import Locators
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, InvalidSelectorException
import time

class Methods(Browser):

    def open_page(self, page):
        self.driver.get(page)
        print("Зашли на сайт " + self.driver.current_url)
        url = self.driver.current_url
        assert url == page

    def spam(self):
        if self.driver.find_element_by_xpath(Locators.LOCATOR_SPAM1).is_displayed():
            self.driver.find_element_by_xpath(Locators.LOCATOR_SPAM1).click()

    def spam3(self):
        try:
            spam_list = [Locators.LOCATOR_SPAM1, Locators.LOCATOR_SPAM3, Locators.LOCATOR_SPAM2]
            time.sleep(5)
            for i in range(0, 3):
                if self.driver.find_element_by_xpath(spam_list[i]).is_displayed():
                    self.driver.find_element_by_xpath(spam_list[i]).click()
                else:
                    continue
        except Exception:
            print(f"Спам отсутствует")
        else:
            print(f"Спам присутствует")

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

    def type_text(self, path, message):
        try:
            field = self.driver.find_element_by_xpath(path)
            field.send_keys(message)
        except Exception as e:
            print(f"Текст {message} не передан по Xpath {path}", format(e))
        else:
            print(f"Текст {message} передан по Xpath {path}")

    def get_text(self, path):
        try:
            text0 = self.driver.find_element_by_xpath(path).text
        except Exception as e:
            print(f"Текст {text0} не извлечен из элемента по Xpath {path}", format(e))
        else:
            print(f"Текст  извлечен из элемента по Xpath {path}")
            return text0

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

    def str_to_float(self, num):
        num_after = float(num.replace(".", "").replace(",", "."))
        return num_after
