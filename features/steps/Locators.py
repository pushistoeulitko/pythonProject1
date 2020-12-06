
class Locators:
    LOCATOR_PATH1 = "//nav[@id='navMenu']//a[text()='Котировки']"
    LOCATOR_PATH2 = "//ul[@class='subMenuNav']//a[text()='Акции']"
    LOCATOR_PATH3 = "//div[@class='navBarDropDown']//a[text()='Россия']"
    LOCATOR_SPAM1 = "//div[@id='PromoteSignUpPopUp']/div[2]/i"
    LOCATOR_SPAM2 = "//div[@id='closeBtn']"
    LOCATOR_SPAM3 = "//i[@class ='popupCloseIcon']"
    LOCATOR_TITLE = "//h1[@class='float_lang_base_1 shortH1 relativeAttr']"
    LOCATOR_COMPANY_NAME = "//td[@class='bold left noWrap elp plusIconTd']"
    LOCATOR_COMPANY_PRICE = "//td[3][starts-with(@class, 'pid')]"
    LOCATOR_LOGIN_FORM = "//span[@id='userAccount']//a[text()='Вход']"
    LOCATOR_EMAIL = "//input[@id='loginFormUser_email']"
    LOCATOR_PASSWORD = "//input[@id='loginForm_password']"
    LOCATOR_ENTER = "//div[@id='loginPopup']//a[text()='Вход']"
    LOCATOR_WARN1 = "//div[@id='serverErrors']"
    LOCATOR_WARN2 = "//div[@id='emailSigningNotify']"
    LOCATOR_DIVIDENTS = "//span[text() = 'Дивиденды']/../span[2]"
    LOCATOR_NAME_DIVIDENTS = f'//td[@class ="bold left noWrap elp plusIconTd"]//a[text()='
