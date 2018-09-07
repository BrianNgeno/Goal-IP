from app import create_app
from flask_script import Manager,Server

#creating app instance
app = create_app('test')

manager = Manager(app)
manager.add_command('serve',Server)

def make_shell_context():
    return dict(app = app)

if __name__ == '__main__':
    manager.run()