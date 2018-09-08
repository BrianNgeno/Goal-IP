from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    usrename = db.Column(db.String(255))

    def __repr__self:
        return f'User{self.username}'