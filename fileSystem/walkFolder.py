# -*- coding: utf-8 -*-
# !/Users/wdai1/Envs/python-everyday-life/bin/python

import pathlib


def tree(root_path_obj):
    assert root_path_obj.is_dir()
    items = list()
    for item in root_path_obj.resolve().iterdir():
        if item.is_dir():
            items.extend(tree(item)) # recursion!
        else:
            items.append(item)
    return items


if __name__ == '__main__':

    rel_myfolder = pathlib.Path('.') / '../Flask-micro-framework-intro-files'
    abs_myfoler = rel_myfolder.resolve()

    print('\nWalking folder: {}'.format(abs_myfoler))
    items = tree(abs_myfoler)
    print('\n'.join([str(i) for i in items]))

    print('\nWalking only the text files in the folder: {}'.format(rel_myfolder))

    for f in rel_myfolder.rglob('*.html'):
        print(f)
    print('\nWalking files whose name starts with __ in the folder: {}'.format(rel_myfolder))
    for f in rel_myfolder.rglob('__*'):
        print(f)

