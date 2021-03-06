from app import create_app, db
from flask_script import Manager, Server
from app.models import User, Role, Pitches, Comments
from  flask_migrate import Migrate, MigrateCommand

# creating app instance

app = create_app('production')
# app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.command 
def test():
    '''
    run the tests for the whole application
    '''
    

    import unittest 
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Role = Role, Pitches = Pitches, Comments = Comments)
    pass


if __name__ == '__main__':
    manager.run()