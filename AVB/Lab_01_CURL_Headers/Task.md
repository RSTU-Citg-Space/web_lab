# HTTP HTTPS и их параметры 
___________________________________________________
## Лабораторная работа №1

В данной работе вы будете отправлять HTTP запросы и изучать HTTP ответы.
### Цель работы
Познакомиться с протоколом HTTP и протоколом HTTPS, а так же особенностями установления соединения между источником и получателем.
___________________________________________________
### Список URL которые мы будем ~~мучить~~ исследовать
- __[‍🎓 РГУПС](https://www.rgups.ru)__
- __[Github](https://github.com/)__
- __[🚝 РЖД](https://www.rzd.ru/)__
- __[🕸 Яндекс](https://yandex.ru/)__
- __[🐍 Python](https://www.python.org/)__
- __[Saint 🌠 GIT](https://git-scm.com/)__
- __[🐵 Jetbrains](https://www.jetbrains.com/)__
- __[💪 VSC - this is best choose](https://code.visualstudio.com/)__

>Заповедь создателя
>>_this list most be continued_

___________________________________________________
### Описание работы
Для работы вам понадобиться **GitBush**, **Браузер** и встроенная утилита **curl**.
Рассмотрим пример отправки http запроса с использованием утилиты **curl**

>**GET** запрос
>```shell
>curl www.exaple.com
>```
>HTTP ответ
>```shell
>  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
>                                 Dload  Upload   Total   Spent    Left  Speed
>100   146  100   146    0     0    433      0 --:--:-- --:--:-- --:--:--   435
><html>
><head><title>403 Forbidden</title></head>
><body>
><center><h1>403 Forbidden</h1></center>
><hr><center>nginx</center>
></body>
></html>
>```
Как видите запрос привёл к получению некоторого html кода, который был бы отрисован браузером и данным о загрузке.
Однако в данном запросе не хватает метта информации которая содержится в заголовках запросов и ответов.

### Ваша задача юные подаваны
_______________________________________________________
Изучите светлую сторону и утилиту **curl**, а затем сделайте запрос, что бы получить следующий формат ответа:
```shell
your code in this place
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 216.58.207.206:80...
* Connected to youtube.com (216.58.207.206) port 80 (#0)
> HEAD / HTTP/1.1
> Host: youtube.com
> User-Agent: curl/7.83.1
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 301 Moved Permanently
< Content-Type: application/binary
< X-Content-Type-Options: nosniff
< Cache-Control: no-cache, no-store, max-age=0, must-revalidate
< Pragma: no-cache
< Expires: Mon, 01 Jan 1990 00:00:00 GMT
< Date: Tue, 06 Sep 2022 16:02:21 GMT
< Location: https://youtube.com/
< Content-Length: 0
< Server: ESF
< X-XSS-Protection: 0
< X-Frame-Options: SAMEORIGIN
<
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0HTTP/1.1 301 Moved Permanently
Content-Type: application/binary
X-Content-Type-Options: nosniff
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Pragma: no-cache
Expires: Mon, 01 Jan 1990 00:00:00 GMT
Date: Tue, 06 Sep 2022 16:02:21 GMT
Location: https://youtube.com/
Content-Length: 0
Server: ESF
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
```
После того как вы это сделаете вам необходимо исследовать форматы ответов при обращении к разным именам хостов:
**Пример для одного ресурса:**
- example.ru
- www.example.ru
- http://example.ru
- https://example.ru
- https://example.ru

Все перечисленные домены в итоге обращаются к одному ресурсу, но формат HTTP ответов будет разным.

В итоге вы должны получить следующую информацию о ресурсе:
- IP адрес веб сервера
- порт к которому вы обращаетесь
- истинное значение хоста ресурса
- информация о необходимости кэширования
- данные о формате данных которые содержатся в теле ответа
- код ответа и его значение
- протокол по которому осуществлялся запрос
- прочая важная информация содержащаяся в заголовке (копайте глубже и найдёте ~~гематоген~~ золото)