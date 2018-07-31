# -*- coding: utf-8 -*-
# !/Users/wdai1/Envs/python-everyday-life/bin/python

import pathlib
import shutil


if __name__ == '__main__':
    file = pathlib.Path('../Flask-micro-framework-intro-files/8-flask-micro-framework-intro-slides.pdf')
    print('Deleting file: {}'.format(file))
    file.unlink()

    folder = pathlib.Path('../Flask-micro-framework-intro-files/8-flask-micro-framework-intro-exercise-files')
    print('Deleting folder: {}'.format(folder))
    shutil.rmtree(str(folder))
