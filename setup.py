import configparser
import os

CONFIG_FILE = os.path.normpath('C:\etc\smart.conf')


def setup():
    print(CONFIG_FILE)
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    ftp_server = config['server']
    print(ftp_server.get('ip'))


if __name__ == '__main__':
    setup()
