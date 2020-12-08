Feature: : Тестовое задание акции, %, дивиденты

  Scenario: Часть 1 (сбор информации о росте цен акций российских кампаний)
    Given Открываем сайт
    When Переходим на вкладку Котировки
    When Переходим на вкладку Котировки->Акции
    When Переходим на вкладку Акции->Россия по "<path>"
    Then Проверяем заголовок
    Then Собираем данные в Json 2
    #Then Собираем данные в Json 1                #не масштабируемое решение
    #Then Выгрузка собранных данных в JSON 1      #не масштабируемое решение
    Then Выгрузка собранных данных в JSON 2
    Then Рассчет изменения цены % в большую сторону
    And Закрываем сайт


  Scenario: Часть 2 (сбор информации о дивидентах акций российских кампаний)
    Given Из Json в Python
    Given Открываем страницу с акциями российских кампаний
    #Given Открываем сайт
    #When Переходим на вкладку Котировки
    #When Переходим на вкладку Котировки->Акции
    #When Переходим на вкладку Акции->Россия по "<path>"
    Then Собираем данные о дивидентах


  Scenario Outline: Часть 3 (тестирование залогинивания)
    Given Открываем сайт
    When Переходим в форму залогинивания
    Then Вводим почту "<email>"
    And Вводим пароль "<password>"
    And Кнопка Войти
    And Заголовок или Предупреждение "<warn>"
    And Закрываем сайт

    Examples:
      | email                     | password | warn                                                              |
      | pushistoeulitko@yandex.ru | 1234567  | "       "                                                         |
      | pushistoeulitko@yandex.ru | " "      | Используйте 4-15 символов, включая как минимум 2 буквы и 2 цифры. |
      | " "                       | " "      | Пожалуйста, введите действительный электронный адрес              |
