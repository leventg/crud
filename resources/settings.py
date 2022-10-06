import logging
import sys
from os import environ

logger = logging.getLogger(__name__)

"""
    Gets environment variables. In case of prod, these env variables should be set.
    If MOCK_DB=='true' the sqlite db is used.
    
    MOCK_DB
    DB_HOST
    DB_NAME
    DB_USER
    DB_PASSWORD
    DB_PORT
"""
server = None
database = None
username = None
password = None
db_port = None
mock_db=None

if not environ.get("DB_HOST") \
    or not environ.get("DB_NAME") \
    or not environ.get("DB_USER") \
    or not environ.get("DB_PASSWORD") \
    or not environ.get("DB_PORT"):
    mock_db='true'
try:
    if environ.get("MOCK_DB"):
        mock_db= str(environ.get("MOCK_DB")).lower()
    server = environ.get("DB_HOST")
    database = environ.get("DB_NAME")
    username = environ.get("DB_USER")
    password = environ.get("DB_PASSWORD")
    db_port = environ.get("DB_PORT")
except:
    logger.critical("Database type is not specified. 'ENVIRONMENT' variable has to be given")
    sys.exit(1000)

args = dict(port=db_port,server=server, user=username, password=password, database=database, charset="utf8", mock_db=mock_db)
