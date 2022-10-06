import os
import sys
from db.sess_prv import dbSessionProvider
from db.tables import Listings
from models.list_mdl import MdlList
from sqlalchemy import false, update
from sqlalchemy.orm import Session
import logging


logger = logging.getLogger(__name__)


class ListService:
    def get_all(self):
        session=dbSessionProvider.cretaeSession()
        res=session.query(Listings).all()
        session.close()
        return res
    def get_by_id(self,id:int):
        session=dbSessionProvider.cretaeSession()
        res=session.query(Listings).filter(Listings.id==id).first()
        session.close()
        return res

    def update(self,mdlList:MdlList):
        session=dbSessionProvider.cretaeSession()
        session.begin()
        res=session.query(Listings).filter(Listings.id==mdlList.id).first()
        updated_item=None
        if res:
            res.address=mdlList.address
            res.price=mdlList.price
            session.commit()
            updated_item = MdlList(id=res.id,address=res.address,price=res.price)
        else:
            session.rollback()
        session.close()
        return updated_item

    def insert(self,mdlList:MdlList):
        session=dbSessionProvider.cretaeSession()
        session.begin()
        rec=Listings()
        rec.id=mdlList.id
        rec.address=mdlList.address
        rec.price=mdlList.price
        ret=True
        try:
            res=session.add(rec)
            session.commit()
        except Exception as ex:
            session.rollback()
            ret=False
        finally:
            session.close()
        return ret

    def delete(self,id:int):
        session=dbSessionProvider.cretaeSession()
        session.begin()
        res=True
        try:
            rec=session.query(Listings).filter(Listings.id==id).first()
            if rec:
                session.delete(rec)
                session.commit()
            else:
                res=False
        except Exception as ex:
            logger.critical('ERROR IN DELETE OP')
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger.critical("Type: {}, Value: {}, Traceback: {}".format(exc_type, fname, exc_tb.tb_lineno))
            logger.critical(ex)
            session.rollback()
            res=False
        session.close()
        return res