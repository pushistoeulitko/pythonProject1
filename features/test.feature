Feature: Тестовое задание акции, %, дивиденты
  #Background: Передаем драйвер
    #Given Открываем сайт

  Scenario: Часть 1 (сбор информации)
    Given Открываем сайт
    When Переходим на вкладку Котировки->Акции->Россия
    Then Проверяем заголовок
    Then Собираем данные в Json 2
    #Then Собираем данные в Json 1
    #Then Выгрузка собранных данных в JSON 1
    Then Выгрузка собранных данных в JSON 2
    And Закрываем сайт


   Scenario Outline: Часть 3 (тестирование залогинивания)
     Given Открываем сайт
     When Переходим в форму залогинивания
     Then Вводим почту "<email>"
     Then Вводим пароль "<password>"
     Then Кнопка Войти
     And  Закрываем сайт

   Examples:
   |  email                       |  password     |
   | pushistoeulitko@yandex.ru    |    1234567    |
   | pushistoeulitko@yandex.ru    |     " "       |
   |          " "                 |   " "         |

