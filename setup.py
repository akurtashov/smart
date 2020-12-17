import configparser
import os
import argparse


CONFIG_FILE = os.path.normpath('C:\etc\smart.conf')


def setup():
    parser = argparse.ArgumentParser(description='Setup initial parameter of smart project')
    parser.add_argument('-c', default='/etc/smart.conf', type=str, help='config file name')
    
    args = parser.parse_args()
    
    config_file = args.c

    print(config_file)
    config = configparser.ConfigParser()
    config.read(config_file)
    ftp_server = config['server']
    print(ftp_server.get('ip'))


if __name__ == '__main__':
    setup()
