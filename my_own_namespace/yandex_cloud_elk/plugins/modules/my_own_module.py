#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Создаёт файл с заданным содержимым

version_added: "1.0.2"

description: Модуль создаёт файл на удалённом хосте по указанному пути.

options:
    path:
        description: Путь к файлу, который будет создан/обновлён.
        required: true
        type: str
    content:
        description: Содержимое файла.
        required: true
        type: str

author:
    - Asadbek Asadbekov (@asad-bekov)
'''

EXAMPLES = r'''
- name: Создать файл test.txt с содержимым
  my_own_module:
    path: /tmp/test.txt
    content: "Hello from custom module!"
'''

RETURN = r'''
changed:
    description: Был ли изменён файл.
    type: bool
    returned: always
msg:
    description: Результат выполнения.
    type: str
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
import os

def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True),
    )

    result = dict(
        changed=False,
        msg=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']

    # Проверка существования и содержимого файла
    file_changed = True
    if os.path.exists(path):
        with open(path, 'r') as f:
            existing_content = f.read()
        if existing_content == content:
            file_changed = False

    if module.check_mode:
        result['changed'] = file_changed
        result['msg'] = 'Check mode: file would be created/updated' if file_changed else 'Check mode: no changes'
        module.exit_json(**result)

    # Создать/обновить файл, если требуется
    if file_changed:
        with open(path, 'w') as f:
            f.write(content)
        result['changed'] = True
        result['msg'] = f'File {path} created/updated.'
    else:
        result['msg'] = f'File {path} already up to date.'

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
