from setuptools import setup
from cqupt import __generation__

setup(
    name='cqupt',
    version=__generation__,
    description='Piper is a command line tool to get info from jwzx.cqupt.edu.cn.',
    author='Mivinci XJJ',
    packages=['cqupt'],
    install_requires=[
        'PrettyTable',
        'requests',
        'bs4'
    ],
    entry_points={
        'console_scripts': [
            'cqupt = cqupt.piper:cli'
        ]
    }
)
