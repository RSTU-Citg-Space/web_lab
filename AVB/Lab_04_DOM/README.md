# Лабораторная работа №4. Основы работы с DOM. Преобразования документов

В этой работе Вы попробуете создавать обработчики событий и модифицировать DOM в зваисимости от происходящих событий.


## Описание работы

Вам предстоит доработать код документа, получившегося в результате лабораторной работы №3, необходимо будет реализовать обработчики событий, которые будут преобразовывать состояние документа и его элементов.

**[Задания по Лабораторной работе №4](https://github.com/RSTU-Citg-Space/web_lab/blob/frontend/AVB/Lab_04_DOM/Task.md)**

### Подсказки по свойствам и методам

* `elem.querySelector(селектор)` - получение одного вложенного элемента, соответствующего селектору
* `elem.querySelectorAll(селектор)` - получение всех элементов, соответствующих селектору
* `elem.onclick(function(){ ... })` - обработчик события клика
* `document` - корневой объект DOM-иерархии
* `elem.scrollTop` - свойство элемента, означающий насколько пикселей проскроллен контент внутри данного элемента
* `elem.getBoundingClientRect()` - метод возвращающий параметры позиционирования элемента относительно окна документа
* `node.append(узлы)` - добавление узла в конец
* `let timerId = setInterval(func|code, [delay], [arg1], [arg2], ...)` - запуск таймера с интервальными срабатывания
* `clearInterval(timerId)` - удаление таймера


## Материалы по теме

* [Цикл for](https://learn.javascript.ru/while-for)
* [Навигация по DOM-элементам](https://learn.javascript.ru/dom-navigation)
* [Поиск элементов в DOM](https://learn.javascript.ru/searching-elements-dom)
* [Изменение документа](https://learn.javascript.ru/modifying-document)
* [Размеры и прокрутка окна](https://learn.javascript.ru/size-and-scroll-window)
* [Основы событий мыши](https://learn.javascript.ru/mouse-events-basics)
* [Таймер]([https://learn.javascript.ru/settimeout-setinterval](https://learn.javascript.ru/settimeout-setinterval#setinterval))
