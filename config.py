import os

class Config:
    
    '''
    General class configurations
    '''
    BASE_URL= 'https://lemasi-books.herokuapp.com/main{}'
    #BASE_URL='http://127.0.0.1:8000/main{}'
 
    SECRET_KEY = os.urandom(12)
    SQLALCHEMY_DATABASE_URI = 'postgres://bptxcxumdfywnp:98c5c2d47ec7ea613332257fd7b61b3136dd5b97f36adda893b9262a77cfd8e9@ec2-34-193-112-164.compute-1.amazonaws.com:5432/dbp1991ff3kg7p'

    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://leresipitchdb:pitchidea@localhost/pitches'
  

    
    
class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
    SECRET_KEY ='lkjelkjdskjdjwjepjdhah'

class DevConfig(Config):

    # SQLALCHEMY_DATABASE_URI = 'postgres://bptxcxumdfywnp:98c5c2d47ec7ea613332257fd7b61b3136dd5b97f36adda893b9262a77cfd8e9@ec2-34-193-112-164.compute-1.amazonaws.com:5432/dbp1991ff3kg7p'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}