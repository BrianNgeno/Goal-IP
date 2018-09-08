from app import create_app,db
from flask_script import Manager,Server
from app.models import User

#creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

@manager.command 
def test():
    '''
    run the tests for the whole application
    '''
    import unittest 
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


def make_shell_context():
    return dict(app = app)

@manage.shell
def make_shell_context():
    return dict (app = app, db = db,User = User)

if __name__ == '__main__':
    manager.run()