import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

# create a user object instead of having dictionarys
# store of data


class UserRegister(Resource):
    # Create request parser that accepts username and password, parse data comminto into post request
    parser = reqparse.RequestParser()

    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )


    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "User with that username already exists."}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201
