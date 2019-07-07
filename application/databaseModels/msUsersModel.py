from application import db
from passlib.hash import pbkdf2_sha256 as sha256
from datetime import datetime



class MSUsersModel(db.Model):
    __tablename__ = 'msusers'

    id = db.Column(db.Integer, primary_key=True)
    msname = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    registration_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'msname': x.msname,
                'password': x.password,
                'registration_date': x.registration_date
            }
        return {'users': list(map(lambda x: to_json(x), MSUsersModel.query.all()))}


    @classmethod
    def find_by_username(cls, msname):
        return cls.query.filter_by(msname=msname).first()
    

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)
    

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)
    

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    
    def __repr__(self):
        return '<msuser {}>'.format(self.msname)
