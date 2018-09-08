from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.Foreignkey('roles.id'))

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.column(db.integer,primary_key = True)
    name = db.column(db.String(255))

    def __repr__(self):
        return f'User{self.name}'