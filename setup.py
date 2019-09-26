from setuptools import setup
from cquptpiper import __generation__

setup(
    name='cquptpiper',
    version=__generation__,
    description='Piper is a command line tool to get info from jwzx.cqupt.edu.cn.',
    author='Mivinci XJJ',
    packages=['cquptpiper'],
    install_requires=[
        'PrettyTable',
        'requests',
        'bs4'
    ],
    entry_points={
        'console_scripts': [
            'cqupt = cquptpiper.piper:cli'
        ]
    }
)
