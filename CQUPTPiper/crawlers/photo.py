from CQUPTPiper.piper import Piper

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
    def __init__(self, stuid: str, piper: Piper):
        self.stuid = stuid
        self.piper = piper
        """
        You can start coding like
            self.config = self.piper.config
            self.session = self.piper.session
        for your convenience.
        """

    def show(self): pass

    def save(self, path: str): pass
