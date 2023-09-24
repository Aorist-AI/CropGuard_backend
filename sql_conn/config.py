from configparser import ConfigParser
import os


def config(filename=os.path.dirname(os.path.abspath(__file__))+'/config.ini', section='mysql'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return db

def weather_config(filename=os.path.dirname(os.path.abspath(__file__))+'/config.ini', section='weather_api'):
     # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to weather api
    weather_api = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            weather_api[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
    
    return weather_api
