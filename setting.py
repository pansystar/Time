from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base


ENGINE = create_engine('postgres://ozqqhdmuqezsca:a220c425e3f1a1ab567bdfb15625642cd33f3ca924a3846352923f45bf39d6ba@ec2-3-208-50-226.compute-1.amazonaws.com:5432/d4p1h3ane0mls4')  
    
session = scoped_session(
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = ENGINE
    )
)

# modelで使用する
Base = declarative_base()
Base.query = session.query_property()