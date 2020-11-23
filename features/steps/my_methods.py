import allure
from selenium.webdriver.common.action_chains import ActionChains
from features.steps.brower_setting import Browser
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, InvalidSelectorException


class Methods(Browser):

    def open_main_page(context):
        context.driver.get('https://ru.investing.com')
        print("Зашли на сайт " + context.driver.current_url)
        assert context.driver.current_url == 'https://ru.investing.com/'

    def spam(context):
        path = "//*[@id='PromoteSignUpPopUp']/div[2]/i"
        if context.driver.find_element_by_xpath(path).is_displayed():
            context.driver.find_element_by_xpath(path).click()

    def screenshots(context):
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    def move_mouse_to_element(context, path):

        try:
            element1 = context.driver.find_element_by_xpath(path)  # Котировки
            hover = ActionChains(context.driver).move_to_element(element1)
            hover.perform()
        except Exception as e:
            print(f"Элемент отсутствует по Xpath {path}", format(e))
        else:
            print(f"Элемент присутствует по Xpath {path}")

    def click_element(context, path):
        try:
            context.driver.find_element_by_xpath(path).click()
        except Exception() as e:
            print(f"Элемент отсутствует по Xpath {path}", format(e))
        else:
            print(f"Элемент присутствует по Xpath {path}")

    def type_text(context, path, messege):
        try:
            field = context.driver.find_element_by_xpath(path)
            field.send_keys(messege)
        except Exception as e:
            print(f"Текст {messege} не передан по Xpath {path}", format(e))
        else:
            print(f"Текст {messege} передан по Xpath {path}")

    def check_word(context, path, word):
        try:
            word_0 = context.driver.find_element_by_xpath(path).text
            assert word in word_0
        except Exception as e:
            print(f"Текст {word}  отсутствует по Xpath {path}", format(e))
        else:
            print(f"Текст {word} присутствует по Xpath {path}")

    def check_elements(context, path):
        try:
            elements = context.driver.find_elements_by_xpath(path)
            number = str(len(elements))
        except Exception as e:
            print(f"Элементы не найдены {path}", format(e))
        else:
            print(f"Найдено элементов: {number}")
            return elements
