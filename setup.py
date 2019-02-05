# coding: utf8

from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(name='yandex_connect',
      version='0.015b',
      description='API Yandex Connect',
      url='http://github.com/zt50tz/yandex-connect',
      author='Alexeev Nick',
      author_email='n@akolka.ru',
      license='MIT',
      packages=['yandex_connect'],
      install_requires=[
            'requests',
            'docutils'
      ],
      zip_safe=False,
      long_description=long_description,
      long_description_content_type='text/markdown'
)
