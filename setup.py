import configparser

config = configparser.ConfigParser()
config.read('/etc/smart.conf')
ftp_server = config['server']
print(ftp_server.get('ip'))
