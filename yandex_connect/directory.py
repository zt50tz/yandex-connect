# coding: utf8

"""
Yandex.Connect Directory API module
:author: Alexeev Nick
:email: n@akolka.ru
:version: 0.01b
"""

from .base import *
from inspect import currentframe


class YandexConnectDirectory(YandexConnectBase):
    """ Yandex connect directory API base class """

    DOMAIN = u'https://api.directory.yandex.net'  # Request Domain

    # ------------------------------------------------------------------------------------------------------------------
    # Helper functions
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def prepare_contacts(contacts):
        """
        Convert contacts list of tuple to yandex data structure
        :param contacts: list[('type', 'value')]
        :return: list
        """
        if not contacts:
            return None
        ret = []
        if contacts:
            for i in range(len(contacts)):
                if type(contacts[i]) is tuple:
                    item = {
                        "type": contacts[i][0],
                        "value": contacts[i][1]
                    }
                else:
                    item = contacts[i]
                ret.append(item)
        return ret

    @staticmethod
    def prepare_name(data):
        """
        Prepare kwargs name words to yandex data structure
        :param data: kwargs of request
        :return: None
        """
        data['name'] = {
            'first': data['name'],
            'last': data['secname'],
            'middle': data['sername']
        }
        for key in data['name'].keys():
            if not data['name'][key]:
                del data['name'][key]
        for key in ['secname', 'sername']:
            del data[key]

    # ------------------------------------------------------------------------------------------------------------------
    # User
    # ------------------------------------------------------------------------------------------------------------------

    def user_info(self, user_id, fields=None):
        """
        Получение информации о сотруднике
        :param user_id: ID
        :param fields: поля, по умолчанию: id, nickname
        :url man: https://tech.yandex.ru/connect/directory/api/concepts/users/read-user-docpage/
        :return: yandex request dict — информация о сотруднике
        """
        data = inspect_args_func(currentframe())
        data['fields'] = self.prepare_fields(data['fields'], 'nickname')
        return self.request('users/%s' % user_id, data, method='get')

    def user_list(self, fields=None, id=None, nickname=None, department_id=None, recursive_department_id=None, group_id=None, recursive_group_id=None, is_dismissed=None, page=None, per_page=None):
        """
        Получение списка сотрудников
        :param fields: поля, по умолчанию id, nickname
        :param id: фильтр
        :param nickname: фильтр
        :param department_id: фильтр
        :param recursive_department_id: фильтр
        :param group_id: фильтр
        :param recursive_group_id: фильтр
        :param is_dismissed: фильтр
        :param page: страница
        :param per_page: на странице
        :url man: https://tech.yandex.ru/connect/directory/api/concepts/users/read-users-list-docpage/
        :return: yandex request dict — список сотрудников
        """
        data = inspect_args_func(currentframe())
        data['fields'] = self.prepare_fields(data['fields'], 'nickname')
        return self.request('users', data, method='get')

    def user_list_full(self, fields=None, id=None, nickname=None, department_id=None, recursive_department_id=None, group_id=None, recursive_group_id=None, is_dismissed=None):
        """
        Получение полного списка сотрудников, без страниц
        :param fields: поля, по умолчанию id, nickname
        :param id: фильтр
        :param nickname: фильтр
        :param department_id: фильтр
        :param recursive_department_id: фильтр
        :param group_id: фильтр
        :param recursive_group_id: фильтр
        :param is_dismissed: фильтр
        :url man: https://tech.yandex.ru/connect/directory/api/concepts/users/read-users-list-docpage/
        :return: yandex request list - список сотрудников
        """
        return self.list_full(self.user_list, 'nickname', **inspect_args_func(currentframe()))
    
    def user_add(self, nickname, password, about=None, aliases=None, birthday=None, contacts=None, department_id=1, gender='male', is_admin=None, is_dismissed=None, name=None, secname=None, sername=None, position=None):
        """
        Добавление сотрудника
        :param nickname: логин
        :param password: пароль
        :param about: описание
        :param aliases: list, ['псевдоним1', ...]
        :param birthday: datetime.date, день рождения
        :param contacts: list, Контакты в типах яндекса, либо [tuple('type', 'value'), ...]
        :param department_id: ID отдела, 1
        :param gender: Пол — male|female
        :param is_admin: bool, Администор
        :param is_dismissed: bool, Увольнение
        :param name: Имя
        :param secname: Фамилия
        :param sername: Отчество
        :param position: Должность
        :url man: https://tech.yandex.ru/connect/directory/api/concepts/users/add-user-docpage/
        :return: yandex request dict — созданный сотрудник
        """
        data = inspect_args_func(currentframe())
        spos = data['nickname'].find('@')
        if spos > -1:
            data['nickname'] = data['nickname'][:spos]
        self.prepare_name(data)
        data['contacts'] = self.prepare_contacts(data['contacts'])
        return self.request('users', data, method='post')

    def user_upd(self, user_id, nickname=None, password=None, about=None, birthday=None, contacts=None, department_id=None, gender=None, is_admin=None, is_dismissed=None, name=None, secname=None, sername=None, position=None):
        """
        Изменение сотрудника
        :param user_id: ID сотрудника
        :param nickname: логин
        :param password: пароль
        :param about: описание
        :param aliases: list, ['псевдоним1', ...]
        :param birthday: datetime.date, день рождения
        :param contacts: list, Контакты в типах яндекса, либо [tuple('type', 'value'), ...]
        :param department_id: ID отдела, 1
        :param gender: Пол — male|female
        :param is_admin: bool, Администор
        :param is_dismissed: bool, Увольнение
        :param name: Имя
        :param secname: Фамилия
        :param sername: Отчество
        :param position: Должность
        :url man: https://tech.yandex.ru/connect/directory/api/concepts/users/edit-user-docpage/
        :return: yandex request dict — измененный сотрудник
        """
        data = inspect_args_func(currentframe())
        self.prepare_name(data)
        data['contacts'] = self.prepare_contacts(data['contacts'])
        return self.request('users/%s' % user_id, data, method='patch')

    def user_alias_add(self, user_id, name):
        """
        Добавление алиаса для сотрудника
        :param user_id: ID сотрудника
        :param name: алиас
        :url man: https://tech.yandex.ru/connect/directory/api/concepts/users/add-user-aliases-docpage/
        :return: yandex request dict
        """
        return self.request('users/%s/aliases' % user_id, inspect_args_func(currentframe()), method='post')

    # ------------------------------------------------------------------------------------------------------------------
    # Department
    # ------------------------------------------------------------------------------------------------------------------

    def department_list(self, fields=None, page=None, per_page=None):
        """
        Получение списка отделов
        :param fields: поля, по умолчанию - id, name
        :param page: страница
        :param per_page: количество элементов на странице
        :url man: https://tech.yandex.ru/connect/directory/api/concepts/departments/read-departments-list-docpage/
        :return: yandex request list - список отделов
        """
        data = inspect_args_func(currentframe())
        data['fields'] = self.prepare_fields(data['fields'], 'name')
        return self.request('departments', data, method='get')

    def department_list_full(self, fields=None):
        """
        Получение полного списка отделов
        :param fields: поля, по умолчанию - id, name
        :url man: https://tech.yandex.ru/connect/directory/api/concepts/departments/read-departments-list-docpage/
        :return: yandex request list - список отделов
        """
        return self.list_full(self.department_list, 'name', **inspect_args_func(currentframe()))

    def department_info(self, department_id):
        """
        Получение информации об отделе
        :param department_id: ID
        :return: yandex request dict
        """
        return self.request('departments/%s' % department_id, method='get')

    def department_add(self, name, label, description=None, head_id=None, parent_id=1):
        """
        Добавление отдела
        :param name: название
        :param label: рассылка
        :param description: описание
        :param head_id: id руководителя отдела
        :param parent_id:  id родительского отдела, 1
        :url man: https://tech.yandex.ru/connect/directory/api/concepts/departments/create-department-docpage/
        :return: yandex request dict - созданный отдел
        """
        return self.request('departments', inspect_args_func(currentframe()), method='post')

    def department_upd(self, department_id, name=None, description=None, head_id=None, label=None, parent_id=None):
        """
        Изменение отдела
        :param department_id: ID
        :param name: название
        :param label: рассылка
        :param description: описание
        :param head_id: id руководителя отдела
        :param parent_id: id родительского отдела
        :url man: https://tech.yandex.ru/connect/directory/api/concepts/departments/edit-department-docpage/
        :return: yandex request dict - созданный отдел
        """
        return self.request('departments/%s' % department_id, inspect_args_func(currentframe()), method='patch')

    def department_del(self, department_id):
        """
        Удаление отдела
        :param department_id: ID
        :url man: https://tech.yandex.ru/connect/directory/api/concepts/departments/delete-department-docpage/
        :return: bool
        """
        return self.request('departments/%s' % department_id, method='delete')

    # ------------------------------------------------------------------------------------------------------------------
    # Group
    # ------------------------------------------------------------------------------------------------------------------

    def group_list(self, fields=None, page=None, per_page=None):
        """
        Список команд
        :param fields: поля, по умолчанию — id, name
        :param page: страница
        :param per_page: на странице
        :url man: https://tech.yandex.ru/connect/directory/api/concepts/groups/read-groups-list-docpage/
        :return: yandex request list - список команд
        """
        data = inspect_args_func(currentframe())
        data['fields'] = self.prepare_fields(data['fields'], 'name')
        return self.request('groups', data, method='get')

    def group_list_full(self, fields=None):
        """
        Полный список команд
        :param fields: поля, по умолчанию — id, name, email
        :url man: https://tech.yandex.ru/connect/directory/api/concepts/groups/read-groups-list-docpage/
        :return: yandex request list - список команд
        """
        if not fields:
            fields = ['name', 'email']
        return self.list_full(self.group_list, 'name', **inspect_args_func(currentframe()))

    def group_info(self, group_id, fields=None):
        """
        Получение информации о команде
        :param group_id: ID
        :param fields: поля, по умолчанию — id, name
        :url man: https://tech.yandex.ru/connect/directory/api/concepts/groups/read-group-docpage/
        :return: yandex request dict - команда
        """
        data = inspect_args_func(currentframe())
        data['fields'] = self.prepare_fields(data['fields'], 'name')
        return self.request('groups/%s' % group_id, data, method='get')

    def group_add(self, name, label, admins=None, description=None, members=None, type=None):
        """
        Добавление команды
        :param name: название команды
        :param label: название рассылки
        :param admins: [{"id": <идентификатор администратора>, "type": "user"},...]
        :param description: описание
        :param members: list — [{"type": "<user|group|department>", "id": <идентификатор>},...]
        :param type: тип - generic|organization_admin|robots|department_head
        :url man: https://tech.yandex.ru/connect/directory/api/concepts/groups/create-group-docpage/
        :return: yandex request dict - созданная команда
        """
        return self.request('groups', inspect_args_func(currentframe()), method='post')

    def group_upd(self, group_id, name=None, label=None, admins=None, description=None, members=None, type=None):
        """
        Изменение команды
        :param group_id: ID
        :param name: название команды
        :param label: название рассылки
        :param admins: [{"id": <идентификатор администратора>, "type": "user"},...]
        :param description: описание
        :param members: list — [{"type": "<user|group|department>", "id": <идентификатор>},...]
        :param type: тип - generic|organization_admin|robots|department_head
        :url man: https://tech.yandex.ru/connect/directory/api/concepts/groups/edit-group-docpage/
        :return: yandex request dict - измененная команда
        """
        return self.request('groups/%s' % group_id, inspect_args_func(currentframe()), method='patch')

    def group_member_list(self, group_id):
        """
        Участники команды
        :param group_id: ID
        :url man: https://tech.yandex.ru/connect/directory/api/concepts/groups/read-group-members-list-docpage/
        :return: yandex request list - участники команды
        """
        return self.request('groups/%s/members' % group_id, method='get')

    def group_member_add(self, group_id, type, id):
        """
        Добавить участника команды
        :param group_id: ID
        :param type: Тип - user|group|department
        :param id: User ID
        :url man: https://tech.yandex.ru/connect/directory/api/concepts/groups/add-group-member-docpage/
        :return: yandex request dict
        """
        return self.request('groups/%s/members' % group_id, inspect_args_func(currentframe()), method='post')

    def group_member_del(self, group_id, user_id):
        """
        Удалить участника команды
        :param group_id: ID
        :param user_id: User ID
        :url man: https://tech.yandex.ru/connect/directory/api/concepts/groups/bulk-add-group-member-docpage/
        :return: True
        """
        return self.group_member_update(group_id, [{'operation_type': 'remove', 'value': {'id': user_id, 'type': 'user'}}])

    def group_member_update(self, group_id, actions):
        """
        Изменение участников команды
        :param group_id: ID
        :param actions: list, [{"operation_type": "<add|remove>", "value": {"type": "<user|group|department>", "id": ID User}},..]
        :url man: https://tech.yandex.ru/connect/directory/api/concepts/groups/bulk-add-group-member-docpage/
        :return: True
        """
        return self.request('groups/%s/members/bulk-update' % group_id, data=actions, method='post')

    # ------------------------------------------------------------------------------------------------------------------
    # Domain
    # ------------------------------------------------------------------------------------------------------------------

    def domain_list(self, fields=None):
        """
        Получение списка доменов
        :param fields: поля, по умолчанию name
        :url man: https://tech.yandex.ru/connect/directory/api/concepts/domains/read-domains-list-docpage/
        :return: yandex request list
        """
        data = inspect_args_func(currentframe())
        data['fields'] = self.prepare_fields(data['fields'], 'name', only_title_field=True)
        return self.request('domains', data, method='get')

    def domain_add(self, name):
        """
        Добавить домен
        :param name: домен
        :url man: https://tech.yandex.ru/connect/directory/api/concepts/domains/add-domain-docpage/
        :return: bool
        """
        return self.request('domains', inspect_args_func(currentframe()), method='post')

    def domain_del(self, name):
        """
        Удалить домен
        :param name: домен
        :url man: https://tech.yandex.ru/connect/directory/api/concepts/domains/delete-domain-docpage/
        :return: bool
        """
        return self.request('domains/%s' % name, method='delete')

    # ------------------------------------------------------------------------------------------------------------------
    # Organization
    # ------------------------------------------------------------------------------------------------------------------

    def organization_list(self, fields=None):
        """
        Список организаций
        :param fields: поля, по умолчанию — id, name
        :return: yandex request list
        """
        data = inspect_args_func(currentframe())
        data['fields'] = self.prepare_fields(data['fields'], 'name')
        return self.request('organizations', data, method='get')['result']
