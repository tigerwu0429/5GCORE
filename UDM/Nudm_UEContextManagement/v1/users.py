# coding: utf-8
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import \
     BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
     DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
     LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
     NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
     TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
import mysql.connector
Base = declarative_base()

# 定义User对象:
class Users(Base):
    # 表的名字:
    __tablename__ = 'users'

    # 表的结构:
    #id = Column(String(20), primary_key=True)
    #name = Column(String(20))
    #sqn = Column(BigInteger(20))
    OPc =  Column(VARBINARY(16))
    imei = Column(VARCHAR(15))
    imsi = Column(String(15),primary_key = True)
