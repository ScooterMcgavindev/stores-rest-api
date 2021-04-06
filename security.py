from werkzeug.security import safe_str_cmp
from models.user import UserModel



# Create 2 functions
# 1: authenticate a user, given a username and password, will select the correct user from the list

def authenticate(username, password):
    user = UserModel.find_by_username(username)          # look in db username
    if user and safe_str_cmp(user.password, password):
        return user

# 2: identity function takes in a payload and the payload is the contents of the jwt token, then extract user id from payload
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)     # retrieve the specific user that matches the payload