# coding: utf8

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='yandex_connect',
      version='0.011b',
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
