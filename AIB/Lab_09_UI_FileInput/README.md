# Лабораторная работа №9. Разработка поля асинхронной загрузки файла на сервер.

В данной работе Вы научитесь работать с нативным средством асинхронного обмена данными между браузером и сервером — XMLHttpRequest.

**[Задания по Лабораторной работе №9](https://github.com/RSTU-Citg-Space/web_lab/blob/frontend/AIB/Lab_09_UI_FileInput/Task.md)**

### Подсказка по HTML-тегам

* `<form enctype="multipart/form-data">` - атрибут `enctype` со значением `multipart/form-data` указывает браузеру не кодировать отправляемые данные, что позволяет передавать файлы.
* `<input type="file">`

### Подсказка по JS

* `document.forms.upload.onsubmit`
* `xhr = new XMLHttpRequest()`
* `xhr.onprogress()`
* `xhr.onload()`
* `xhr.onerror()`
* `xhr.upload`


## Материалы по теме
* [XMLHttpRequest: индикация прогресса](https://learn.javascript.ru/xhr-onprogress)
