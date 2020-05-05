# from app import app


# if __name__ == "__main__":
#     app.run()


from app import app
from flask import Flask
from flask_script import Manager

manager = Manager(app)

@manager.command
def dev():
    from livereload import Server
    live_server = Server(app.wsgi_app)  # app.wsgi_app 即 app.run()
    live_server.watch("**/*.*")
    live_server.serve(open_url=False)

if __name__ == "__main__":
    manager.run()