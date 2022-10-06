
import logging
import os
import sys
from sqlalchemy import create_engine, engine_from_config,text
from sqlalchemy.orm import sessionmaker,Session,Query
from resources.settings import args
from db.tables import Base

logger =logging.getLogger(__name__)
class SessionProvider:
    """
        Session provider class. Ensures fair session usage. 
        Populates mock_db if used
        provides global  dbSessionProvider class
    """
    def __init__(self) -> None:
        try:
            env_keys=args.keys()
            if  args['mock_db'] == 'true':
                
                # mock_db, sq lite
                connection_string = "sqlite:///db/crud.db"
                if os.path.exists("db/crud.db"):
                    os.remove("db/crud.db")

            else:
                connection_string = '{0}:{1}@{2}:{3}/{4}'.format(args['user'],args['password'],args['server'],args['port'],args['database'])
                connection_string = "postgresql+psycopg2://{}?options=-csearch_path%3Ddbo,public".format(connection_string)
            
            self.engine = create_engine(connection_string)

            
            Base.metadata.create_all(self.engine)
            self.my_sessionmaker:Session = sessionmaker(bind=self.engine, expire_on_commit=False)
        except Exception as ex:
            logger.critical(f"can not to connect database-connection_string:"+connection_string)
            logger.critical('ERROR IN DB CONNECTION')
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger.critical("Type: {}, Value: {}, Traceback: {}".format(exc_type, fname, exc_tb.tb_lineno))
            logger.critical(ex)

            sys.exit(1000)
        
        if  args['mock_db'] == 'true':
            # create table
            con=self.engine.connect()
            
            with open("./db/create.sql") as file:
                query = text(file.read())
                con.execute(query)
            
            # insert seed values
            with open("./db/seed.sql") as file:
                query = text(file.read())
                con.execute(query)

    def cretaeSession(self)->Session:
        return self.my_sessionmaker()
     
dbSessionProvider=SessionProvider()