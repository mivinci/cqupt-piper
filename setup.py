from setuptools import setup, find_packages
from cqupt import __generation__

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='cqupt',
    version=__generation__,
    description='CQUPT Piper is a command line tool to get info from jwzx.cqupt.edu.cn',
    long_description=long_description,
    long_description_content_type="text/markdown",
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
