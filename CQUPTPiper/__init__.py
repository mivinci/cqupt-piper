from pathlib import Path


__piper__ = 'CQUPT-Piper'
__author__ = 'Mivinci XJJ'
__version__ = '0.0.1'
__year__ = '2019.9'
__description__ = f'{__piper__} v{__version__} @{__author__} {__year__}'

# SHELL_PREFIX = '\033[92m>\033[0m '
SHELL_PREFIX = '>>> '


PIPER_DIR = f'{Path.home()}/.piper'
PIPER_PATH = f'{PIPER_DIR}/piper'
PIPER_CAPTCHA_PATH = f'{PIPER_DIR}/captcha.png'
