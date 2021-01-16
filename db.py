from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#engine = create_engine('mysql://root:zaq12wsx@localhost:13306/flask_test?charset=utf8', echo=True)
engine = create_engine(' mysql://ba899f3b32b533:cd7a8319@us-cdbr-iron-east-01.cleardb.net:3306/ad_752a490146a72e0', echo=True)

DB_Session = sessionmaker(bind=engine)
db_session = DB_Session()
Base = declarative_base()


def init_db():
    import models
    Base.metadata.create_all(bind=engine)


def drop_db():
    Base.metadata.drop_all(engine)


def initial_db():
    drop_db()
    init_db()


if __name__ == '__main__':
    init_db(engine)