from setuptools import setup

setup(
    name='piper',
    description='Piper is a command line tool to get info from jwzx.cqupt.edu.cn.',
    author='Mivinci XJJ',
    packages=['piper'],
    entry_points={
        'console_scripts': [
            'piper = CQUPTPiper.piper:cli'
        ]
    }
)
