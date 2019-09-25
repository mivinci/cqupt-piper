from setuptools import setup
from CQUPTPiper import __version__

setup(
    name='cquptpiper',
    version=__version__,
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
            'piper = cquptpiper.piper:cli'
        ]
    }
)
