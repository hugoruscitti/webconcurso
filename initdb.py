# coding=utf-8
from app.db.project import ProjectTable
from app.db import db_engine, db_session

try:
    ProjectTable.__table__.create(bind=db_engine)
    db_session.add(ProjectTable('Hola mundo!!!'))
    db_session.add(ProjectTable(u'hola!'))
    db_session.commit()
except:
    pass
