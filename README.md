## О сервере
С помощью flask реализована команда `/dictionary`.

 __формат запроса__ `{'key': str, 'value': str}`


 __формат ответа сервера__ `{'result': str, 'time': str}`

### GET
* при GET запросе по урлу `/dictionary/{key}` сервер возвращает значение из dictionary, соответствующее ключу key
* в случае отсутствия key в dictionary возвращается ответ со статусом кода 404 и описанием проблемы.

### POST
* при POST запросе в указанном формате по урлу `/dictionary` в словарь вставляется ключ и значение
* сервер возвращает значение из dictionary, соответствующее ключу key, и время ответа
* в случае существование key в dictionary возвращается ответ со статусом кода 409 и описанием проблемы

### PUT
* при PUT запросе в указанном формате по урлу `/dictionary/{key}` в словаре обновляется значение ключа 
* сервер возвращает значение из dictionary, соответствующее ключу key, и время ответа
* в случае отсутствия key в dictionary возвращается ответ со статусом кода 404 и описанием проблемы.

### DELETE
* при DELETE запросе по урлу `/dictionary/{key}` сервер удаляет значение из dictionary, соответствующее ключу key
* в случае отсутствия key в dictionary возвращается ответ со статусом кода 200
* сервер возвращает в поле result - None и время ответа

## Тестирование 
__Запуск в консоли__ `pytest`

__Просмотр allure отчета__ `allure serve allure`

* реализованы 4 класса для каждого из методов 
* протестированы статусы кода, валидные и невалидные формы тела запроса, валидые и невалидные урлы, функциональность методов 
* реализованы фикстуры для прямого взаимодействия со словарем 









 
