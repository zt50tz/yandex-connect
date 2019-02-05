# yandex_connect

Библиотека python для использования API Yandex connect / Яндекс коннект.
В настоящий момент реализованы все функции Directory, версии 6.

https://tech.yandex.ru/connect/directory/api/about-docpage/

### Установка

```bash
git clone https://github.com/zt50tz/yandex-connect
cd yandex-connect
sudo python setup.py install
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
app = YandexConnectDirectory('<OAuth TOKEN>', org_id=None)  # создание
app.user_add('test', 'test234test')  # добавление сотрудника
app.user_list_full()  # просмотр всех сотрудников
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
- ```group_member_add``` - Добавить участника команды
- ```group_member_del``` - Удалить участника команды
- ```group_member_update``` - Изменение участников команды

##### Домены
- ```domain_list``` - Получение списка доменов
- ```domain_add``` - Добавить домен
- ```domain_del``` - Удалить домен

##### Организации
- ```organization_list``` - Список организаций
