# Шпаргалка
_______________________________________________________________________
### Основные типы данных
Целочисленный тип
```python
int
int('12') # преобразует в число 12
```
Вещественные числа
```python
float
float('12.8') # преобразует в число 12.8
float(12) # преобразует в число 12.0
```
Строковые переменные
```python
str
str(12) # преобразует в строку '12'
str([1, 2, 3]) # преобразует в строку '[1, 2, 3]'
# в строку можно преобразовать почти всё
```
Булевые переменные
```python
bool
bool(12) # преобразует в True
12 == 12 # True
12 == 13 # False
str(0) # преобразует в False
``` 
_______________________________________________________________________
### Коллекции
Списки (__mutable__)
```python
list
data = list()
data = []
data = [1, 12.0, 'string', [2, 3], True, None]
data[0] # -> 1
data[-1] # -> None
data.append('element') # [1, 12.0, 'string', [2, 3], True, None, 'element']
``` 
Кортеж (__immutable__)
```python
tuple
data = tuple()
data = 1, 2, 'string', [2,3], True, None # (1, 2, 'string', [2, 3], True, None)
data[1] # -> 2
data[-2] # -> True
```
Словарь (хэш таблица) (__mutable__)
```python
dict
data = {}
data = {1: '1', 'string': 2, True: False, (4, 5): [8, 6], None: {1: 1, 2: '2'}}
data[1] # '1'
data['string'] # 2
data[None][1] # 1
```
Множество (__mutable__)
```python
set()
data = set()
data = set(
    (91, None, 'string', True, (1, 3))
)
# unordered
```
_______________________________________________________________________
### Циклы
цикл с предусловием, в условии логическое выражение
```python
while True:
    print('infinity')
```
цикл поддерживающий протокол итерации
```python
result = 0
for i in range(10):
    result += i
# result = 45
```
_______________________________________________________________________
### Функции
```python
def function(arg1, arg2, *args, **kwargs):
    # arg1 - первый позиционный аргумент
    # arg2 - второй позиционный аргумент
    # *args - последующие позиционные аргументы преобразуются в кортеж
    # **kwargs - последующие именованные аргументы преобразуются в словарь
    result = f'{arg1} {arg2}'
    print(result)
    print(args) # tuple
    print(kwargs) # dict
    return result # возвращение результат работы
    
function('first', 2, 3, 4, 5, 6, a='key', b='value')
# first 2
# (3, 4, 5, 6)
# {'a': 'key', 'b': 'value'}
```

_______________________________________________________________________
### Декорирование
```python
# простой декоратор для функции с параметрами
def decorator(func):
    def wrapped(*args, **kwargs):
        print('I am decorated')
        return func(*args, **kwargs)
    return wrapped

@decorator
def my_func(first, second):
    print(first)
    print(second)

my_func(1, 2)

# I am decorated
# 1
# 2
```
