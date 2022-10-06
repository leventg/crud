# crud
Create, Read, Update, Delete project for Listings table.

# directory structure
```
root
|
|
----> db
|      |
|      -----> create.sql: table creation sql file
|             crud.db: sqlite database file
|             seed.sql: listings table data population (insert) file  
|             sess_prv.py: session provider, which export dbSessionProvider gloval var as a factory instance for session.  
|             tables.py: sqlalchemy table definition file
|
----> logs
|      |
|      -----> main.log: log file. definition is in resources/logging.conf
|       
----> main.py: application entry file
----> test_empty.py:placeholder for pytest
----> README.md:this file
----> requirements.txt:required packages for pip
|
|
----> models
|      |
|      -----> list_mdl.py: Presetation layer input-output model 
|
----> resources  
|      |
|      ----->logging.conf: conficuration file for logging. for details please refer to logging documents
|            settings.py: environment varaibles expected from environment
|
----> services
|      |
|      -----> list_serv.py: service for listing table
|
----> test (pytest is used: all test files should be in this directory)
       |
       -----> test_main.py: tests for main.py 
```
# usage
```
FastAPI is used for detailed description please refer to the FastApi documents
In order to run use one of the following methods:
1. uvicorn main:router
2. ptyhon -m main

In order to test:
pytest
```
# assumptions
```
If environment variables are not provided or all variables provided and MOCK_DB=='true' then mock_db environment variable is set to true.
  In this case:
    1. sqlite is used as mock_db 
    2. db/crud.db created.
    3. listings table created 
    4. seed.sql is populated
otherwise: It is assumed that connection information for an existing PostgreSQL database is provided.
In that case the following environment parameters should be populated:
    MOCK_DB: 'true'|'false' (if true sqlite is used) 
    DB_HOST: database host name
    DB_NAME: database name
    DB_USER: db user
    DB_PASSWORD: password
    DB_PORT: port
```
