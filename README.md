# pythonProject1

Тестовое задание 

Стек: Python >3.7, behave, selenium, chromedriver, sqlite3, flask
Исходные данные: stocks (файл sqlite)

Данное тестовое задание мы постарались адаптировать под наши текущие задачи, проблемы в процессе автоматизации. Итак, приступим к описанию задачи:
Часть 1
Вам необходимо написать тестовый сценарий, который собирает информацию (название, цена) на сайте (https://ru.investing.com/) о российских акциях, цена которых изменилась  на определенный % в большую сторону. Цена для расчета % роста цен, хранится в базе данных stocks (данные по акциям находятся по следующему пути Котировки->Акции->Россия). При переходе к  списку акций проверять отсутствие / присутствие заголовка Россия – акции. После сбора информации сценарий должен выгрузить собранные данные в файл report.json
Важное замечание: запрещается использовать прямые ссылки на необходимые страницы, использовать только итерации по web-сайту. 
Часть 2
Следующий сценарий должен запускаться в 4 экземплярах параллельно, при этом на вход он должен получать название компании из ранее сохраненного файла (report.json) для последующего использования в шагах. 
У компаний, собранных в части 1, необходимо найти дивидендную доходность в %  и сохранить в переменную, финальный отчет должен формироваться после окончания прогона всех сценариев (данные собраны по всем компаниям из файла report.json). Формат отчета следующий: название компании, доходность
 
Часть 3
Также необходимо протестировать форму входа, прогнать сценарии со всем тестовыми наборами 3шт. Например: (user1, password1), (user2, password2) и т.д. (проверку формы вынести в отдельный сценарий):
•	Поля не заполнены (проверка предупреждающего сообщения)
•	Поле email заполнено (проверить предупреждающее сообщение)

Разработать веб-интерфейс для предоставления визуальной информации из данных json-отчета, используйте flask, дизайн на ваше усмотрение. Данные, которые нужно отобразить:
•	Название Сценария 
•	Статус сценария
•	Кол-во шагов
•	Время прохождения
Для отчета по акциям:
•	Название компании
•	Доходность

Примечания:
•	Предусмотреть возможность запуска сценариев в различных браузерах (Chrome, Firefox), возможность запуска в headless режиме при установке соответствующей опции.
•	Для поиска элементов использовать XPATH
•	В конце прогона сформировать тестовый отчет в формате json.
•	Создание скриншота на каждом шаге
•	Предусмотреть сценарий, который не будет проходить (понадобится в отчетах)
•	Шаги по возможности должны быть универсальными
•	При поиске элементов выводить отладочную информацию (XPATH – искомого элемента)
•	% изменения цены акции должен указываться в сценарии.
•	При сборе данных из списка акций Вы будете иметь дело с однотипными элементами, у которых вам понадобятся некоторые значения, остается придумать как это унифицировать. (ООП приветствуется)
•	Особое внимание будет обращаться на подход к проектированию архитектуры автотестов (универсальность, переиспользование, простота расширения функциональности).
•	Шаги должны быть на русском языке

Организовать класс Хранилище, для работы с данными во время сценария.
•	Предусмотреть возможность вывода размера хранилища.
•	Загрузка данных из базы при инициализации класса.
•	Возможность сохранения/получения данных из сценария по ключу 
•	Выгрузка данных в файл
