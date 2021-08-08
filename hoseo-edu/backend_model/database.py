#!/usr/bin/python
# -*- coding: utf-8 -*-
print ("module [backend_model.database] loaded")
from datetime import datetime, timedelta
import random
import hashlib


from flask_sqlalchemy import SQLAlchemy

# To solve deadlock
class SQLiteAlchemy(SQLAlchemy):
    def apply_driver_hacks(self, app, info, options):
        options.update({
            'isolation_level': 'READ UNCOMMITTED',
        })
        super(SQLiteAlchemy, self).apply_driver_hacks(app, info, options)

class DBManager:
    db = None

    @staticmethod
    def init(app):
        # print "-- DBManager init()"
        db = SQLiteAlchemy(app)
        DBManager.db = db

    @staticmethod
    def init_db():
        # print "-- DBManager init_db()"
        db = DBManager.db
        db.drop_all()
        db.create_all()
        DBManager.insert_dummy_data()

    @staticmethod
    def clear_db():
        # print "-- DBManager clear_db()"
        DBManager.db.drop_all()

    @staticmethod
    def insert_dummy_data():
        print ('insert_dummy_data')
        DBManager.insert_dummy_user()

    @staticmethod
    def password_encoder(password):
        pass1 = hashlib.sha1(password).digest()
        pass2 = hashlib.sha1(pass1).hexdigest()
        hashed_pw = "*" + pass2.upper()
        return hashed_pw

    @staticmethod
    def get_random_date():
        end = datetime.utcnow()
        start = end + timedelta(days=-60)

        random_date = start + timedelta(
            # Get a random amount of seconds between `start` and `end`
            seconds=random.randint(0, int((end - start).total_seconds())),
        )

        return random_date

    @staticmethod
    def password_encoder_512(password):
        h = hashlib.sha512()
        h.update(password.encode('utf-8'))
        return h.hexdigest()

    @staticmethod
    def get_random_ip():
        ip_list = [u'28.23.43.1', u'40.12.33.11', u'100.123.234.11', u'61.34.22.44', u'56.34.56.77', u'123.234.222.55']

        return ip_list[random.randrange(0, 6)]

    @staticmethod
    def gen_datetime(min_year=2019, max_year=datetime.now().year):
        # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
        start = datetime(min_year, 1, 1, 00, 00, 00)
        years = max_year - min_year + 1
        end = start + timedelta(days=365 * years)
        return start + (end - start) * random.random()

    def generate_token(userID):
        m = hashlib.sha1()

        m.update(userID.encode('utf-8'))
        m.update(datetime.now().isoformat().encode('utf-8'))

        return m.hexdigest()

    def insert_dummy_user():
        print ("insert_dummy_user")
        from backend_model.table_user import Users

        user = Users()
        user.user_id = "admin"
        user.user_pw = DBManager.password_encoder_512('111111')
        user.user_name = "admin"
        user.user_type = 1
        user.phone = "010-1234-5678"
        DBManager.db.session.add(user)

        user = Users()
        user.user_id = "admin2"
        user.user_pw = DBManager.password_encoder_512('111111')
        user.user_name = "admin2"
        user.user_type = 1
        user.phone = "010-1234-5678"
        DBManager.db.session.add(user)

        user = Users()
        user.user_id = "admin3"
        user.user_pw = DBManager.password_encoder_512('111111')
        user.user_name = "admin3"
        user.user_type = 1
        user.phone = "010-1234-5678"
        DBManager.db.session.add(user)

        for i in range(1, 100):
            user = Users()
            user.user_id = "USER" + str(i)
            user.user_pw = DBManager.password_encoder_512('111111')
            user.user_name = "user" + str(i)
            user.user_type = 2
            user.user_status = random.randrange(1, 3)
            user.company = "COMPANY" + str(i)
            user.phone = "010-1234-5678"
            user.email = "user" + str(i) + "@patent.com"
            DBManager.db.session.add(user)

        DBManager.db.session.commit()