from os import remove
from PIL import Image
from CQUPTPiper.subcommand import NameSpace
from CQUPTPiper.auth import KEY_STUID
from CQUPTPiper import PIPER_DIR

URL_PHOTO_WYZ = 'https://raw.githubusercontent.com/Mivinci/cqupt-piper/master/assert/th.jpeg'

"""
Target Url: 'http://jwzx.cqu.pt/showstupic.php?xh={stu_id}'
            also available at piper.urls.URL_STUDENT_PHOTO

Parameter: 'piper' contains attribute that may be needed:
    session: stores all the cookies given by the jwzx server-end
    config:  has the necessary system information and user information
             see at CQUPTPiper.config.Config
    urls:    has the necessary jwzx urls for crawling data
"""
class PhotoCrawler:
    def __init__(self, piper, namespace: NameSpace):
        """
        If user input 'get photo 2018213056 -s -g'
        namespace will be assigned to a dict:
        {
            'get': {
                'option': 'photo',
                'argument': '2018213056',
                'flags': ['-s', '-g'],
            }
        }
        """
        self.namespace = namespace
        self.piper = piper
        """
        You can start coding like
            self.config = self.piper.config
            self.session = self.piper.session
            self.cookies = self.session.cookies
        for your convenience.
        """
        self.user = piper.config.user
        self.stuid = namespace.get('argument') or self.user.get(KEY_STUID)
        self.url = f'{piper.urls.URL_STUDENT_PHOTO}{self.stuid}'

        self.url = URL_PHOTO_WYZ if self.stuid == '2017213056' else self.url

    def fmt_print(self):
        path: str = f'{PIPER_DIR}/a_{self.stuid}.jpg'
        with open(path, 'wb') as f:
            f.write(self.piper.session.get(self.url).content)
        im = Image.open(path)
        im.show()
        remove(path)

    def save(self, path: str): pass
