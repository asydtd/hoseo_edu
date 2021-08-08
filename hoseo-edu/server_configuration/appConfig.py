#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib


class CommonConfig(object):
    pass

class DevelopmentConfig(CommonConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://dbadmin:p@ssw0rd@127.0.0.1:3306/hoseoedudb'

class ProductionConfig(CommonConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://dbadmin:p@ssw0rd@127.0.0.1:3306/hoseoedudb'
