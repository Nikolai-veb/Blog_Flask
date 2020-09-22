class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URL = 'psql+psycopg2-binary://flask:240396@localhost/test_flask'

