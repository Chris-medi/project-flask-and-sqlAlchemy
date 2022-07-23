from flask import Flask

from database import database

from apps.blueprints.users_router import user_route

app =  Flask(__name__)

app.config.from_object('config.DevelopmentConfig')

app.register_blueprint(user_route)

database.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)