# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Python工程的样例包',
    long_description=readme,
    author='Eugene Wang',
    author_email='eugenewyj@163.com',
    url='https://github.com/eugenewyj/eugene-python-samples',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
