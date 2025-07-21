## Описание

В коллекции реализован кастомный модуль `my_own_module` для создания файлов на целевом хосте, а также роль, использующая этот модуль.

## Состав

- modules/my_own_module.py — модуль для создания файла
- roles/my_own_role — роль с использованием модуля

## Использование

### Пример playbook для роли:

```yaml
- name: Использовать роль из коллекции
  hosts: localhost
  gather_facts: false
  roles:
    - role: my_own_namespace.yandex_cloud_elk.my_own_role
      vars:
        my_own_module_path: "/tmp/example.txt"
        my_own_module_content: "Hello from my collection!"
```
		
### Пример прямого использования модуля:

```yaml
- name: Тест my_own_module
  hosts: localhost
  tasks:
    - name: Создать файл через кастомный модуль
      my_own_namespace.yandex_cloud_elk.my_own_module:
        path: /tmp/example2.txt
        content: "Created via custom module"
```

## Установка

`ansible-galaxy collection install <my_own_namespace>.tar.gz`

## Автор
Asad Asadbekov
