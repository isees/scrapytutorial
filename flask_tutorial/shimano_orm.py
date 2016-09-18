from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqlconnector://root:SniperX4@localhost:3306/scrapy', pool_recycle=3600)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Shimano(Base):
    __tablename__ = 'shimano'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    name_md5 = Column(String)


# # default
# engine = create_engine('mysql://scott:tiger@localhost/foo')
#
# # mysql-python
# engine = create_engine('mysql+mysqldb://scott:tiger@localhost/foo')
#
# # MySQL-connector-python
# engine = create_engine('mysql+mysqlconnector://scott:tiger@localhost/foo')
#
# # OurSQL
# engine = create_engine('mysql+oursql://scott:tiger@localhost/foo')
#
# engine = create_engine('mysql+mysqlconnector://root:SniperX4@localhost:3306/scrapy', pool_recycle=3600)

# DBSession = sessionmaker()
# DBSession.configure(bind=engine)
# Base.metadata.create_all(engine)
#
# double_handler = Shimano(id=62)
# tough_handler = Shimano(id=63)
# session = DBSession()
# session.add_all([double_handler, tough_handler])
# session.commit()

# list = Shimano.query.filter(Shimano.id == 63)
# for u in list:
#     print u.id, u.name, u.name_md5
