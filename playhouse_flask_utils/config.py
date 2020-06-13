import os

from yaml import load, Loader

with open(os.path.join(os.path.dirname(__file__),
                       'settings_prod.yml'), 'r') as f:
    settings = load(f, Loader=Loader)
    print(settings)

DATABASES = {
    'dbname': settings['databases']['default']['database'],
    'mysql': {
        'user': settings['databases']['default']['user'],
        'password': settings['databases']['default']['passwd'],
        'host': settings['databases']['default']['host'],
        'port': settings['databases']['default']['port']
    }
}


class Config(object):
    DATABASE_URL = 'mysql://{}:{}@{}:{}/{}'.format(
        DATABASES['mysql']['user'],
        DATABASES['mysql']['password'],
        DATABASES['mysql']['host'],
        DATABASES['mysql']['port'],
        DATABASES['dbname']
)
