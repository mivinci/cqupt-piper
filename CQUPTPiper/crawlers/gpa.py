from CQUPTPiper.subcommand import NameSpace

"""
Target Url: 'http://jwzx.cqu.pt/student/chengjiPm.php' 
            with id='cjAllTab-zypm'
            also available at piper.urls.URL_GPA

Parameter: 'piper' contains attribute that may be needed:
    session: stores all the cookies given by the jwzx server-end
    config:  has the necessary system information and user information
             see at CQUPTPiper.config.Config
    urls:    has the necessary jwzx urls for crawling data

Method: 'fmt_print'
The crawler must have a 'fmt_print' method,
which prints result like

If year specified:
    学期   必修课平均分  非任选课平均分  平均绩点  排名
    20171   xx.xx        xx.xx       x.xx    xxx
    20172   xx.xx        xx.xx       x.xx    xxx
If year not specified:
    学期   必修课平均分  非任选课平均分  平均绩点  排名
    20171   xx.xx        xx.xx       x.xx    xxx
    20172   xx.xx        xx.xx       x.xx    xxx
    20181   xx.xx        xx.xx       x.xx    xxx

    <根据排名的提示>

You DON'T have get the result formatted 100 percent like this.
"""
class GPACrawler:
    def __init__(self, piper, namespace: NameSpace):
        """
        If user input 'get gpa 2018 -s -g'
        namespace will be assigned to a dict:
        {
            'get': {
                'option': 'gpa',
                'argument': '2018',
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
        for your convenience.
        """

    def fmt_print(self): pass
