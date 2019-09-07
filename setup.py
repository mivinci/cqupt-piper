from setuptools import setup
from CQUPTPiper import __version__

setup(
    name='piper',
    version=__version__,
    description='Piper is a command line tool to get info from jwzx.cqupt.edu.cn.',
    author='Mivinci XJJ',
    packages=['CQUPTPiper'],
    entry_points={
        'console_scripts': [
            'piper = CQUPTPiper.piper:cli'
        ]
    }
)
