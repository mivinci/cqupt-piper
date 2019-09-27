from setuptools import setup, find_packages
from cqupt import __generation__

setup(
    name='cqupt',
    version=__generation__,
    description='CQUPT Piper is a command line tool to get info from jwzx.cqupt.edu.cn',
    author='Mivinci XJJ',
    url='https://github.com/mivinci/cqupt-piper',
    packages=find_packages(),
    install_requires=[
        'PrettyTable',
        'requests',
        'bs4'
    ],
    python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            'cqupt = cqupt.piper:cli'
        ]
    }
)
