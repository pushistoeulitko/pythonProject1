from selenium import webdriver
from selenium.webdriver import chrome, firefox
from selenium.webdriver.chrome.options import Options


class Browser(object):

    def settings(context, browser, headless=False):
        path = 'C://Users//pushi//PycharmProjects//'
        if browser == chrome:
            context.driver = webdriver.Chrome(executable_path=path + 'chromedriver.exe')
        elif browser == firefox:
            context.driver = webdriver.Firefox(executable_path=path + 'geckodriver.exe')

        chrome_options = Options()
        if headless == True:
            chrome_options.add_argument("--headless")
            print("Запуск в headless режиме")
        else:
            print("Запуск в браузере")
            context.driver.implicitly_wait(15)
            context.driver.maximize_window()

        #context.driver = webdriver.Chrome(options=chrome_options)

    def quit(context):
        context.driver.quit()  # context.driver.close()
