# coding: utf8

from setuptools import setup

setup(name='yandex_connect',
      version='0.01b',
      description='API Yandex Connect',
      url='http://github.com/zt50tz/yandex-connect',
      author='Alexeev Nick',
      author_email='n@akolka.ru',
      license='MIT',
      packages=['yandex_connect'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
