import json
import logging
import logging.config
import logging.handlers


logging.config.fileConfig('resources/logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)  

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

import uvicorn
from models.list_mdl import MdlList


from services.list_serv import ListService


router = FastAPI(prefix="/listings",
    tags=["listings"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

origins = [
    "http://localhost",
    "http://localhost:5000",
    "http://127.0.0.1:5000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

router.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@router.get("/listing/", tags=["listing"])
async def read_listing():
    retSet=ListService().get_all()
    return retSet


@router.get("/listing/{id}", tags=["listing"])
async def read_listing(id:int):
    ret=ListService().get_by_id(id)
    if ret:
        return ret
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@router.patch("/listing/", tags=["listing"],response_model=MdlList)
async def update_list(item: MdlList):
    ret=ListService().update(item)
    if ret:
        return ret
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@router.delete("/listing/{id}", tags=["listing"],response_model=bool)
async def delete_list(id:int):
    ret=ListService().delete(id)
    if ret==False:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return True

@router.post("/listing/", tags=["listing"], response_model=bool)
async def insert_list(item: MdlList):
    ret=ListService().insert(item)
    if ret:
        return True
    else:
        raise HTTPException(status_code=409, detail="Item not found") 


if __name__ == "__main__":
    config = uvicorn.Config("main:router", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()