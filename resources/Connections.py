import ConfigParser
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import cx_Oracle

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

LAST_ID_COPIED_COL_NAME = 'LAST_ID_COPIED'
OWNER_COL_NAME = 'OWNER_NAME'
RESOURCE_COL_NAME = 'RESOURCE_NAME'

_query = 'select * from ITAYW1_TOP1_MS.PITON'

"""[{'col1': val1, 'col2': 'val2', 'colX': 'valX'}, {...}, {'...'}] """
def parseTuplesFronCursor(_resultSet):
    columns = [i[0] for i in _resultSet.description]
    return [dict(zip(columns, row)) for row in _resultSet]


def parseToReturnObj(tuples):
    owners = []

    for tup in tuples:
        owners.append(tup[OWNER_COL_NAME])

    return {'owners' : owners}

def loadSettings():
    config = ConfigParser.ConfigParser()

    # read the config.ini
    if not config.read(os.path.join(BASE_DIR, 'resources', 'config.ini')):
        raise IOError, 'cannot load config.ini'
    connection = getPitonConnection(config)
    try:
        _resultSet = loadPitonData(connection)
        tuples = parseTuplesFronCursor(_resultSet)

        return parseToReturnObj(tuples)

    except:
        print 'exception occurred'

    finally:
        connection.close()


def loadPitonData(connection):
    cursor = connection.cursor()
    cursor.execute(_query)
    return cursor


def getPitonConnection(config):
    url = '%s/%s@%s:%s/%s' % (config.get('piton_home', 'username'), config.get('piton_home', 'password'),
                              config.get('piton_home', 'server'), config.get('piton_home', 'port'),
                              config.get('piton_home', 'sid'))
    connection = cx_Oracle.connect(url)
    return connection
