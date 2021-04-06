from setuptools import setup, find_packages

setup(
    name='davetestpython',
    version='0.1.0',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'zope.deprecation==4.4.0',
    ]
)
