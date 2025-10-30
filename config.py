import os

class Config:
    if os.environ.get('DATABASE_URL'):
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    else:
        # For local development with MySQL (XAMPP)
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/eventify_db'
        
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    SECRET_KEY = os.environ.get("SECRET_KEY") or "my_SeCrEt_keY"
    
    
class DevelopmentConfiguration(Config):
    debug = True
