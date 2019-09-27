from cqupt.urls import URL_STUDENT_PHOTO
from cqupt.auth import Auth
from cqupt.log import loading
from cqupt import PIPER_HOME
from PIL import Image
from os import remove


white_list: dict = {
    '2017213056': 'https://raw.githubusercontent.com/Mivinci/cqupt-piper/master/assert/th.jpeg'
}


@loading('正在获取照片')
def get_photo(request, stuid: str):
    url: str = ''
    if stuid in white_list:
        url = white_list.get(stuid)
    else:
        url= f'{URL_STUDENT_PHOTO}{stuid}'
    return request.get(url).content


class Photo:
    user: dict = Auth.load_user()

    @classmethod
    def handle(cls, request, arg):
        stuid: str = cls.user.get('userid') if arg == 'self' else arg
        path: str = f'{PIPER_HOME}/photo_{stuid}.jpg'

        with open(path, 'wb') as f:
            f.write(get_photo(request, stuid))
        
        photo = Image.open(path)
        photo.show()
        remove(path)

        
        
        