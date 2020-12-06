from selenium import webdriver
from selenium.webdriver import chrome, firefox
from selenium.webdriver.chrome.options import Options


class Browser(object):

    def settings(self, browser, headless=False):
        path = 'C://Users//pushi//PycharmProjects//'
        if browser == chrome:
            self.driver = webdriver.Chrome(executable_path=path + 'chromedriver.exe')
        elif browser == firefox:
            self.driver = webdriver.Firefox(executable_path=path + 'geckodriver.exe')

        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
            print("Запуск в headless режиме")
        else:
            print("Запуск в браузере")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()

    def quit(context):
        context.driver.quit()  # context.driver.close()
