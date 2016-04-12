import ConfigParser
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import cx_Oracle

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
_query = 'select * from ITAYW1_TOP1_MS.PITON'


def parseData(_resultSet):
    returnedData = dict()
    for row in _resultSet:




def loadSettings():
    config = ConfigParser.ConfigParser()

    # read the config.ini
    if not config.read(os.path.join(BASE_DIR, 'resources', 'config.ini')):
        raise IOError, 'cannot load config.ini'
    connection = getPitonConnection(config)
    try:
        _resultSet = loadPitonData(connection)
        data = parseData(_resultSet)


    except:
        print 'exception occurred'

    finally:
        connection.close()


def loadPitonData(connection):
    cursor = connection.cursor()
    cursor.execute(_query)

    for row in cursor:
        print row

    return ['f', 'g']


def getPitonConnection(config):
    url = '%s/%s@%s:%s/%s' % (config.get('piton_home', 'username'), config.get('piton_home', 'password'),
                              config.get('piton_home', 'server'), config.get('piton_home', 'port'),
                              config.get('piton_home', 'sid'))
    connection = cx_Oracle.connect(url)
    return connection
