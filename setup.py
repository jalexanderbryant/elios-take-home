from setuptools import setup

setup(
    name='elios',
    packages=['application'],
    include_package_data=True,
    install_requires=[
        'flask',
        'sqlalchemy',
    ],
)
