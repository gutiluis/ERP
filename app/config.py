import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", # use the environment variable or the below line of code
        "mysql+pymysql://erp:erp@db:3306/erp"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

'''
username: erp
password: erp
host: db
port: 3306
database: erp
'''