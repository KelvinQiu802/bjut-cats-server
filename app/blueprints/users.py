from flask import Blueprint, request, jsonify, Response
from models.users import Users
from extentions import db


users = Blueprint('users', __name__)


@users.get('/<openId>')
def get_user(openId) -> Response:
    user: Users = Users.query.get(openId)
    if (user != None):
        return user.toDict()
    else:
        return Response(status=404, response='User Not Found')


@users.post('/')
def create_user() -> Response:
    new_user = Users(**request.json)
    db.session.add(new_user)
    db.session.commit()
    return Response(status=201, response=f'User <openId: {request.json["openId"]}> Created')
