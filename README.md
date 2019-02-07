# yandex_connect

Библиотека python для использования API Yandex connect / Яндекс коннект.
В настоящий момент реализованы все функции Directory, версии 6.

https://tech.yandex.ru/connect/directory/api/about-docpage/

### Установка

```bash
git clone https://github.com/zt50tz/yandex-connect
cd yandex-connect
python setup.py install
```

Либо:

```bash
pip install yandex-connect
```


### Получение токена

Необходимо зарегистрировать приложение на странице https://oauth.yandex.ru/

```python
from yandex_connect import token_get_by_code
token_get_by_code()
```


### Пример

```python
from yandex_connect import YandexConnectDirectory
api = YandexConnectDirectory('<OAuth TOKEN>', org_id=None)  # создание
api.user_add('test', 'test234test')  # добавление сотрудника
api.user_list_full()  # просмотр всех сотрудников
```

Сервис использует идентификационные номера для всех объектов, а не
значимые алиасы, что может быть усложняющим фактором при быстрой
разработке, либо при исполнении функций из командной строки. То есть,
для того, чтобы получить информацию о пользователе, необходимо выполнить
следующий код:

```python
api.user_info(1000000000000000)

>> {u'nickname': u'test', u'id': 1000000000000000}
```

Он не особо удобный для чтения и написания. В связи с этим добавлена
возможность выполнить и такой код:

```python
api.user_info('test@test.ru')

>> {u'nickname': u'test', u'id': 1000000000000000}
```

Так же, это справедливо для методов относительно групп. То есть, вместо:
```python
api.group_member_add(1, 1000000000000000)
```

Можно написать:
```python
api.group_member_add("group_users@test.ru", "test@test.ru")
```

Везде где используются параметры ```user_id``` и ```group_id``` можно
использовать как ID, так и почту.

### Отладка
Что то может пойти не так. Чтобы увидеть какие данные уходят и
возвращаются, можно использовать следующий код:

```python
import logging
logger = logging.getLogger('YandexConnectRequest')
logger.setLevel(logging.DEBUG)
```


Методы
------

##### Сотрудники
- ```user_info``` — Получение информации о сотруднике
- ```user_list``` - Получение списка сотрудников
- ```user_list_full``` - Получение полного списка сотрудников, без страниц
- ```user_add``` - Добавление сотрудника
- ```user_upd``` - Изменение сотрудника
- ```user_alias_add``` - Добавление алиаса для сотрудника

##### Отделы
- ```department_list``` - Получение списка отделов
- ```department_list_full``` - Получение полного списка отделов
- ```department_info``` - Получение информации об отделе
- ```department_add``` - Добавление отдела
- ```department_upd``` - Изменение отдела
- ```department_del``` - Удаление отдела

##### Команды
- ```group_list``` - Список команд
- ```group_list_full``` - Полный список команд
- ```group_info``` - Получение информации о команде
- ```group_add``` - Добавление команды
- ```group_upd``` - Изменение команды
- ```group_member_list``` - Участники команды
- ```group_member_add``` - Добавить участника команды. В качестве
параметра ```user_id``` можно использовать массив ID/почт.
- ```group_member_del``` - Удалить участника команды
- ```group_member_update``` - Изменение участников команды

##### Домены
- ```domain_list``` - Получение списка доменов
- ```domain_add``` - Добавить домен
- ```domain_del``` - Удалить домен

##### Организации
- ```organization_list``` - Список организаций
