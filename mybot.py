import requests
import utils
from lxml import html


class MyBot:
    '''Class to login to the website and go to the specific page
    '''
    def __init__(self, username, password):
        self.hostname = 'https://censys.io'
        self.login_path = '/login'
        self.username = username
        self.password = password
        self.csrf_token = ''
        self.get_data = ''
        self.session = ''

    def login(self):
        '''Check if csrf token is obtained, try to login'''
        # retry = 3
        if self.csrf_token != '':
            payload = {'login': '', 'password': '', 'csrf_token': self.csrf_token}
            while retry:
                post_data = requests.post(self.hostname + self.login_path, payload, cookie=dict(self.data.cookies))
                # retry -= 1
        elif self.retry:
            self.connect()

    def connect(self):
        '''Create a new session and connect to login page,
        obtain csrf_token'''
        try:
            self.session = requests.Session()
            self.get_data = self.session.get(self.hostname + self.login_path)
            tree = html.fromstring(self.get_data.text)
            if self.get_data.status_code != 200:
                utils.log(self.status_code)
        except Exception as e:
            raise e
            utils.log('connection error')
        self.csrf_token = list(set(tree.xpath("//input[@name='csrf_token']/@value")))[0]
        utils.log(self.csrf_token)
