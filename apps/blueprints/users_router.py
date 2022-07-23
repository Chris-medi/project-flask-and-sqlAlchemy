import flask
from flask import Blueprint,request,jsonify
from apps.models.user_models import UsersModel
from apps.schemas.schemas_users import UserSchema
from database.database import db
user_route = Blueprint('users',__name__)

from psycopg2.errors import UniqueViolation,IntegrityError
from sqlalchemy.exc import IntegrityError
import json


@user_route.route('/users')
def resquetAllUser():
    query = UsersModel.query.all()
    result = UserSchema(many=True).dump(query)
    return jsonify({"messages":'list users',"data":result})




@user_route.route('/register',methods=['POST'])
def requestRegister():
        data = request.get_json()
        try:
            user = UsersModel(name=data['name'],email=data['email'],password=data['password'])
            db.session.add(user)
            db.session.commit()
        except IntegrityError as e:
            return jsonify({"message":'email o email ya han sido tomados',"details":str(e).split('\n')[1]}),403
        return jsonify({"data":'succes creation user'}),203

@user_route.route('/loggin',methods=['POST'])
def requestLoggin():
    data = request.get_json()
    user = UsersModel.query.filter_by(email=data['email']).first()
    jsonUser = UserSchema().dump(user)

    if user and user.verify_password(data['password']):
        return jsonify({'messages': 'user logeado',"data":jsonUser}), 200
    else:
        return jsonify({'name': 'incorrect credentials'}), 403

