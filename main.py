import sys
from mybot import MyBot
import utils


class CScraper:
    def __init__(self):
        self.bot = MyBot(self.username, self.password).login()


if __name__ == '__main__':
    utils.load_args()
    utils.log(utils.args)
    CScraper(sys.argv[1], sys.argv[2])
