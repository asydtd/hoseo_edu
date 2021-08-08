# -*- coding: utf-8 -*-

print ("module [backend_model.table_patent.py] loaded")
from backend_model.database import DBManager
import datetime

db = DBManager.db


class TB_SENSOR_UPLOAD(db.Model):
    __tablename__ = 'tb_sensor_upload'

    id = db.Column('id', db.Integer, primary_key=True)
    sender_ip = db.Column('sender_ip', db.String(128))
    company_id = db.Column('company_id', db.String(128))
    sensors_msg = db.Column('sensors_msg', db.String(2048))
    created_date = db.Column('created_date', db.DateTime)

class TB_SENSOR_UPLOAD_ENCRYPT(db.Model):
    __tablename__ = 'tb_sensor_upload_encrypt'

    id = db.Column('id', db.Integer, primary_key=True)
    sender_ip = db.Column('sender_ip', db.String(128))
    company_id = db.Column('company_id', db.String(128))
    sensors_msg = db.Column('sensors_msg', db.String(2048))
    created_date = db.Column('created_date', db.DateTime)

