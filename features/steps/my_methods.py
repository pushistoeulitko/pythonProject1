from selenium.webdriver.common.action_chains import ActionChains
from features.steps.brower_setting import Browser

class Methods(Browser):

    def open_main_page(context):
        context.driver.get('https://ru.investing.com')
        print(context.driver.current_url)
        assert context.driver.current_url == 'https://ru.investing.com/'  # "Зашли на сайт"
        path = "//i[@class='popupCloseIcon largeBannerCloser']"

        # if context.driver.find_elements(By.XPATH, path).isDisplayed():
        # context.driver.find_elements(By.XPATH, path).click()

        # if context.driver.find_element_by_xpath("//*[@id='PromoteSignUpPopUp']/div[2]/i").isDisplayed():
        # context.driver.find_element_by_xpath("//*[@id='PromoteSignUpPopUp']/div[2]/i").click()

    def move_mouse_to_element(context, path):
        try:
            element1 = context.driver.find_element_by_xpath(path)  # Котировки
            hover = ActionChains(context.driver).move_to_element(element1)
            hover.perform()
            print(f"Элемент присутствует по Xpath {path}")
        except Exception as e:
            print(f"Элемент отсутствует по Xpath {path}", format(e))

    # NoSuchElementException

    def click_element(context, path):
        try:
            context.driver.find_element_by_xpath(path).click()
            print(f"Элемент присутствует по Xpath {path}")
        except Exception as e:
            print(f"Элемент отсутствует по Xpath {path}", format(e))

    def type_text(context, path, messege):
        try:
            field = context.driver.find_element_by_xpath(path)
            field.send_keys(messege)
            print(f"Текст {messege} передан по Xpath {path}")
        except Exception as e:
            print(f"Текст {messege} не передан по Xpath {path}", format(e))

    # rowsCompanyName = context.driver.find_elements_by_xpath("//td[@class='bold left noWrap elp plusIconTd']")
    # rowsCompanyPrice = context.driver.find_elements_by_xpath("//td[3][starts-with(@class, 'pid')]")
    # print(len(rowsCompanyName), len(rowsCompanyPrice))

    def check_elements(context, path):
        try:
            elements = context.driver.find_elements_by_xpath(path)
            number = str(len(elements))
            print(f"{number} элементов найдено")
            return elements
        except Exception as e:
            print(f"Элементы не найдены {path}", format(e))
