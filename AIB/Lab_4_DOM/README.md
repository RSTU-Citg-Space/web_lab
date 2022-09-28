# Лабораторная работа №4. Работа с DOM.

### Подсказки по CSS-стилям

* `display: fixed` - зафиксированные объекты
* `display: none` - не отображаемые объекты

### Подсказки по HTML

Любым валидным HTML-тегам можно добавлять практически любые пользовательские атрибуты, содержащие мета-данные конкретно этого тега, для этого начинайте название вашего атрибута с `data-`, например, если вам требуется идентификатор `data-id="12"`

### Подсказки по JavaScript

* `for (let item of array) { тело цикла }`
* `elm.onclick = function() { обработчик клика по elm }`
* `elm.addEventListener("click", function() { обработчик клика по elm })`
* `elm.dataset` - массив data-атрибутов элемента
* `str.split(delimeter)` - разбиение строки на массив строк, в качестве разделителя используется строка delimeter
* `arr.find(function(item){ функция сопоставления })` - проверка всех элементов массива на соответствие каждого из них функции сопоставления, если совпадений не найдено - undefined

## Материалы по теме

* https://developer.mozilla.org/ru/docs/Web/API/EventTarget/addEventListener
* https://learn.javascript.ru/array#perebor-elementov
* https://learn.javascript.ru/dom-attributes-and-properties#nestandartnye-atributy-dataset
* https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Global_Objects/String/split
* https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Global_Objects/Array/find
